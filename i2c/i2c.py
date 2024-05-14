from ctypes import POINTER, c_int16, c_uint32

import matplotlib.pyplot as plt
import numpy as np

from picosdk.ps2000 import ps2000
from picosdk.functions import assert_pico2000_ok
from picosdk.PicoDeviceEnums import picoEnum
from picosdk.ctypes_wrapper import C_CALLBACK_FUNCTION_FACTORY

import time
import os
import subprocess
import shutil
import csv
import re

CALLBACK = C_CALLBACK_FUNCTION_FACTORY(
    None,
    POINTER(POINTER(c_int16)),
    c_int16,
    c_uint32,
    c_int16,
    c_int16,
    c_uint32
)

adc_values = []
IDLE_VOLTAGE = 3.5

def get_overview_buffers(buffers, _overflow, _triggered_at, _triggered, _auto_stop, n_values):
    adc_values.extend(buffers[0][0:n_values])


callback = CALLBACK(get_overview_buffers)


def adc_to_volts(values, range_, bitness=16):
    v_ranges = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

    return [x * v_ranges[range_] / (2**(bitness - 1) - 1) for x in values]

def capture_waveforms(device, run_time_ms=1000):
    adc_values.clear()
    
    res = ps2000.ps2000_run_streaming_ns(
        device.handle,
        500,
        2,
        100_000,
        False,
        1,
        50_000
    )
    assert_pico2000_ok(res)

    start_time = time.time_ns()

    while (time.time_ns() - start_time) < (run_time_ms * 1e6):
        ps2000.ps2000_get_streaming_last_values(
            device.handle,
            callback
        )

    end_time = time.time_ns()

    ps2000.ps2000_stop(device.handle)

    v_values = adc_to_volts(adc_values, ps2000.PS2000_VOLTAGE_RANGE['PS2000_5V'])
    
    timeline = np.linspace(0, (end_time - start_time) * 1e-6, len(v_values))
    
    return [timeline, v_values]

def save_waveform_csv(timeline, v_values, folder_name, subfolder_name, file_name):    
    min_length = min(len(timeline), len(v_values))

    with open(f'{folder_name}/{subfolder_name}/{file_name}', 'w') as f:
        f.write('Time,Channel A\n(ms),(V)\n\n')
        for i in range(min_length):
            f.write(f'{timeline[i]},{v_values[i]}\n')

def upload_arduino_code(code, com_port, fqbn):
    try:
        print(f"Attempting to upload code to Arduino on {com_port}.")

        temp_dir = "temp_sketch"
        
        os.makedirs(os.path.join("i2c" ,temp_dir), exist_ok=True)

        sketch_file = os.path.join(os.path.join("i2c" ,temp_dir), f"{temp_dir}.ino")
        with open(sketch_file, "w") as file:
            file.write(code)

        cmd = [
            "arduino-cli", "compile", "--fqbn", fqbn,
            "--port", com_port, os.path.join("i2c" ,temp_dir)
        ]
        try:
            subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as err:                                                                                                   
            if err.returncode == 1:
                print("Error compiling code. Trying different version.")
                shutil.rmtree(os.path.join("i2c" ,temp_dir))
                return -1

        cmd = [
            "arduino-cli", "upload", "--fqbn", fqbn,
            "--port", com_port, os.path.join("i2c" ,temp_dir)
        ]
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)

        print("Code uploaded successfully.")

        shutil.rmtree(os.path.join("i2c" ,temp_dir))

    except subprocess.CalledProcessError as e:
        print("Error uploading code:", e.output.decode())
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

def is_waveform_in_center(v_values, idle_voltage, min_points):
    n = len(v_values)
    center_start = n // 4
    center_end = n - (n // 4)

    center_values = v_values[center_start:center_end]
    num_points_below_threshold = sum(1 for v in center_values if v < idle_voltage - 1.0)

    return num_points_below_threshold >= min_points
   
def auto_capture_waveforms(device, folder_name, subfolder_name, board_name, board_letter, message, run_time_ms=1000):
    waveform_count = 0
                    
    while waveform_count < 64:
        timeline, v_values = capture_waveforms(device, run_time_ms)
        
        if is_waveform_in_center(v_values, IDLE_VOLTAGE, 4):
            csv_filename = f"{board_name}_{board_letter}_{message}_{waveform_count + 1:02d}.csv"
            
            save_waveform_csv(timeline, v_values, folder_name, subfolder_name, csv_filename)

            waveform_count += 1

messages = ["U", "HELLO", "WORLD"]
arduino_code_template = '''
#include <Wire.h>

char buffer[] = "{}";

void setup() {{
    Wire.begin();
}}

void loop() {{
    Wire.beginTransmission(4);
    Wire.write(buffer);
    Wire.endTransmission();
    delay(100);
}}
'''

def replace_whitespace_with_underscore(input_string):
    return re.sub(r'\s+', '_', input_string)

def i2c_record_data(isArduino=False, fqbn="arduino:avr:mega"):
    board_name = replace_whitespace_with_underscore(input("Enter the board name: ")).lower()
    board_letter = input("Enter the desired board letter: ")
    
    if isArduino:
        com_port = input("Enter the COM port (e.g., 'COM3'): ")

    folder_name = os.path.join("i2c", "i2c_data", board_name)
    os.makedirs(folder_name, exist_ok=True)

    with ps2000.open_unit() as device:
        print('Device info: {}'.format(device.info))

        res = ps2000.ps2000_set_channel(
            device.handle,
            picoEnum.PICO_CHANNEL['PICO_CHANNEL_A'],
            True,
            picoEnum.PICO_COUPLING['PICO_DC'],
            ps2000.PS2000_VOLTAGE_RANGE['PS2000_5V']
        )
        assert_pico2000_ok(res)

        for message in messages:
            subfolder_name = f"{board_name}_{board_letter}_{message}"
            os.makedirs(os.path.join(folder_name, subfolder_name), exist_ok=True)

            if isArduino:
                arduino_code = arduino_code_template.format(message)
                resp = upload_arduino_code(arduino_code, com_port, fqbn)

                if resp == -1:
                    arduino_code = arduino_code_template.format(message)
                    upload_arduino_code(arduino_code, com_port, fqbn)
                    
                print("Waiting for the Arduino to start sending the message...")
                time.sleep(5)
            else:
                print("Waiting for the device to start sending the message...")
                time.sleep(5)

            auto_capture_waveforms(device, folder_name, subfolder_name, board_name, board_letter, message, 100)