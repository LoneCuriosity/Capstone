# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:08:57 2023

@author: Jorge Castillo
@Editor: Ramon Garcia
"""
import os
import pandas as pd
pd.options.display.float_format = '{:,.10f}'.format
from framework import USARTConfig, BoardExperiment, I2CConfig, SPIConfig

output = ""
config = None

#C:\Users\ramga\Downloads\picosdk-python-wrappers-master\picosdk-python-wrappers-master\ps2000Examples\Capstone\usart\usart_data\arduino_mega
folder = input("Please enter the folder path: ")
protocal = input("Please enter the protocal used for the dataset: \n1. USART\n2. I2C\n3. SPI\n").lower()  
avg_voltage = float(input("Please enter the average voltage of the device: "))
        
if protocal == "usart":  
    for dirs in os.listdir(folder):        
        output = os.path.join(folder, r"datasets", dirs)
        
        config = USARTConfig(8, 0, 1, int(os.path.join(folder,dirs).split('\\')[-1]), avg_voltage)
        
        datasets = []
        for file in os.listdir(os.path.join(folder,dirs)):
            exp = BoardExperiment('{}/{}'.format(os.path.join(folder,dirs), file), label=file.split("_")[-2], conf=config)
            dataset = exp.create_dataset()
            datasets.append(dataset)

        df = pd.concat(datasets, axis=0).sample(frac=1).reset_index(drop=True)
        os.makedirs(output)
        df.to_csv('{}\{}'.format(output, 'boards_dataset.csv'), float_format='%.10f', index=False)
        print("Dataset for {} created successfully".format(dirs) + " output at: " + output + "\n")
        
elif protocal == "i2c":
    output = os.path.join(folder, r"datasets")
    config = I2CConfig(avg_voltage)
    datasets = []
    for file in os.listdir(folder):
        exp = BoardExperiment('{}/{}'.format(folder, file), label=file.split("_")[-2], conf=config)
        dataset = exp.create_dataset()
        datasets.append(dataset)

    df = pd.concat(datasets, axis=0).sample(frac=1).reset_index(drop=True)
    os.makedirs(output)
    df.to_csv('{}\{}'.format(output, 'boards_dataset.csv'), float_format='%.10f', index=False)
    print("Dataset for I2C created successfully" + " output at: " + output + "\n")
    
elif protocal == "spi":
    output = os.path.join(folder, r"datasets")
    config = SPIConfig(avg_voltage)
    datasets = []
    for file in os.listdir(folder):
        exp = BoardExperiment('{}/{}'.format(folder, file), label=file.split("_")[-2], conf=config)
        dataset = exp.create_dataset()
        datasets.append(dataset)

    df = pd.concat(datasets, axis=0).sample(frac=1).reset_index(drop=True)
    os.makedirs(output)
    df.to_csv('{}\{}'.format(output, 'boards_dataset.csv'), float_format='%.10f', index=False)
    print("Dataset for SPI created successfully" + " output at: " + output + "\n")