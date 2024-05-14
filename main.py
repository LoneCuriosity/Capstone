from usart.usart import usart_record_data
from i2c.i2c import i2c_record_data
from spi.spi import spi_record_data
import subprocess

data_collection_options = ["usart", "i2c", "spi"]

print("Device data collector version 1.0")
print("This program will collect data from the device and save it to a CSV file.")
print("Please ensure that the device is connected to the computer.")
print("Created by: Ramon Garcia")

isArduino = input("Is the device an Arduino? (y/n): ").lower() == "y"
fqbn = ""

if isArduino:
    cmd = ["arduino-cli", "board", "list"]
    print(subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode())
    fqbn = input("Enter the FQBN of the Arduino: ")
    
    
protocal = ""
while protocal not in data_collection_options:
    protocal = input("Enter the data collection protocal (USART, I2C, SPI): ").lower()
        
if protocal == "usart":
    usart_record_data(isArduino, fqbn)
elif protocal == "i2c":
    i2c_record_data(isArduino, fqbn)
elif protocal == "spi":
    spi_record_data(isArduino, fqbn)
            