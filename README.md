# Capstone-Project - Serial Device Identification

## Requirments
|Software|version|
|---|---|
|miniconda| conda - 24.3.0 |
|arduino-cli| 10.0.22631.3527 |
|Python| 3.12.2 |

## Installtion
First, make sure to download and install the picosope SDK from the picoscope webpage. Follow the Get Started section within this repository.
https://github.com/picotech/picosdk-python-wrappers

Once done make sure you have installed miniconda and the arduino-cli. Next open miniconda and run the following command.
```sh
conda env update -n capstone --file env.yml
```

The file env.yml is located within the root of the repository. This command will set up the environment and install the packages needed along with the correct version of Python. Once installed activate the environment using the following command.

```sh
conda activate capstone
```

## Run
To start collecting data just run the main.py file within the root directory this program will walk you through collecting data from any board. __One thing to note is that the program is fully automated for Arduino boards meaning that it will auto-install the scripts onto the board and automate other tasks. For none, Arduino boards the user must upload the sending and receiving code. The receiving code for the Arduino also has to be manually installed.__

```sh
python main.py
```

The program will walk you through the different required inputs. For asking you whether you are using an Arduino board if so providing the correct FQBN from the list presented you should select the board that is sending the message not receiving it. Which protocol do you want to use? The program will then ask you for more specific information about the board like what is the name of the board (AKA Arduino Mega, Arduino Uno, etc..) it will also ask you about which board letters to use since we may be using mutiple of the same board but each board should have a unique letter. (AKA A, B, C). Finally, the program may ask you for a COM port for which the sending device is using.

## Folder structure

```bash
├───feature extraction
│   └───__pycache__
├───i2c
│   ├───i2c_data
│   │   ├───arduino_due
│   │   │   ├───arduino_due_A_HELLO
│   │   │   ├───arduino_due_A_U
│   │   │   ├───arduino_due_A_WORLD
│   │   │   ├───arduino_due_B_HELLO
│   │   │   ├───arduino_due_B_U
│   │   │   ├───arduino_due_B_WORLD
│   │   │   ├───arduino_due_C_HELLO
│   │   │   ├───arduino_due_C_U
│   │   │   ├───arduino_due_C_WORLD
│   │   │   └───datasets
│   │   └───arduino_mega
│   │       ├───arduino_mega_A_HELLO
│   │       ├───arduino_mega_A_U
│   │       ├───arduino_mega_A_WORLD
│   │       ├───arduino_mega_B_HELLO
│   │       ├───arduino_mega_B_U
│   │       ├───arduino_mega_B_WORLD
│   │       ├───arduino_mega_C_HELLO
│   │       ├───arduino_mega_C_U
│   │       ├───arduino_mega_C_WORLD
│   │       ├───arduino_mega_D_HELLO
│   │       ├───arduino_mega_D_U
│   │       ├───arduino_mega_D_WORLD
│   │       └───datasets
│   └───__pycache__
├───machine learning
├───spi
│   ├───spi_data
│   │   ├───arduino_due
│   │   │   ├───arduino_due_A_HELLO
│   │   │   ├───arduino_due_A_U
│   │   │   ├───arduino_due_A_WORLD
│   │   │   ├───arduino_due_B_HELLO
│   │   │   ├───arduino_due_B_U
│   │   │   ├───arduino_due_B_WORLD
│   │   │   ├───arduino_due_C_HELLO
│   │   │   ├───arduino_due_C_U
│   │   │   ├───arduino_due_C_WORLD
│   │   │   └───datasets
│   │   └───arduino_mega
│   │       ├───arduino_mega_A_HELLO
│   │       ├───arduino_mega_A_U
│   │       ├───arduino_mega_A_WORLD
│   │       ├───arduino_mega_B_HELLO
│   │       ├───arduino_mega_B_U
│   │       ├───arduino_mega_B_WORLD
│   │       ├───arduino_mega_C_HELLO
│   │       ├───arduino_mega_C_U
│   │       ├───arduino_mega_C_WORLD
│   │       └───datasets
│   └───__pycache__
└───usart
    ├───usart_data
    │   ├───arduino_due
    │   │   ├───115200
    │   │   │   ├───arduino_due_A_HELLO
    │   │   │   ├───arduino_due_A_U
    │   │   │   ├───arduino_due_A_WORLD
    │   │   │   ├───arduino_due_B_HELLO
    │   │   │   ├───arduino_due_B_U
    │   │   │   ├───arduino_due_B_WORLD
    │   │   │   ├───arduino_due_C_HELLO
    │   │   │   ├───arduino_due_C_U
    │   │   │   └───arduino_due_C_WORLD
    │   │   ├───19200
    │   │   │   ├───arduino_due_A_HELLO
    │   │   │   ├───arduino_due_A_U
    │   │   │   ├───arduino_due_A_WORLD
    │   │   │   ├───arduino_due_B_HELLO
    │   │   │   ├───arduino_due_B_U
    │   │   │   ├───arduino_due_B_WORLD
    │   │   │   ├───arduino_due_C_HELLO
    │   │   │   ├───arduino_due_C_U
    │   │   │   └───arduino_due_C_WORLD
    │   │   ├───9600
    │   │   │   ├───arduino_due_A_HELLO
    │   │   │   ├───arduino_due_A_U
    │   │   │   ├───arduino_due_A_WORLD
    │   │   │   ├───arduino_due_B_HELLO
    │   │   │   ├───arduino_due_B_U
    │   │   │   ├───arduino_due_B_WORLD
    │   │   │   ├───arduino_due_C_HELLO
    │   │   │   ├───arduino_due_C_U
    │   │   │   └───arduino_due_C_WORLD
    │   │   └───datasets
    │   │       ├───115200
    │   │       ├───19200
    │   │       └───9600
    │   └───arduino_mega
    │       ├───115200
    │       │   ├───arduino_mega_A_HELLO
    │       │   ├───arduino_mega_A_U
    │       │   ├───arduino_mega_A_WORLD
    │       │   ├───arduino_mega_B_HELLO
    │       │   ├───arduino_mega_B_U
    │       │   ├───arduino_mega_B_WORLD
    │       │   ├───arduino_mega_C_HELLO
    │       │   ├───arduino_mega_C_U
    │       │   ├───arduino_mega_C_WORLD
    │       │   ├───arduino_mega_D_HELLO
    │       │   ├───arduino_mega_D_U
    │       │   ├───arduino_mega_D_WORLD
    │       │   ├───arduino_mega_X_HELLO
    │       │   ├───arduino_mega_X_U
    │       │   └───arduino_mega_X_WORLD
    │       ├───19200
    │       │   ├───arduino_mega_A_HELLO
    │       │   ├───arduino_mega_A_U
    │       │   ├───arduino_mega_A_WORLD
    │       │   ├───arduino_mega_B_HELLO
    │       │   ├───arduino_mega_B_U
    │       │   ├───arduino_mega_B_WORLD
    │       │   ├───arduino_mega_C_HELLO
    │       │   ├───arduino_mega_C_U
    │       │   ├───arduino_mega_C_WORLD
    │       │   ├───arduino_mega_D_HELLO
    │       │   ├───arduino_mega_D_U
    │       │   ├───arduino_mega_D_WORLD
    │       │   ├───arduino_mega_X_HELLO
    │       │   ├───arduino_mega_X_U
    │       │   └───arduino_mega_X_WORLD
    │       ├───9600
    │       │   ├───arduino_mega_A_HELLO
    │       │   ├───arduino_mega_A_U
    │       │   ├───arduino_mega_A_WORLD
    │       │   ├───arduino_mega_B_HELLO
    │       │   ├───arduino_mega_B_U
    │       │   ├───arduino_mega_B_WORLD
    │       │   ├───arduino_mega_C_HELLO
    │       │   ├───arduino_mega_C_U
    │       │   ├───arduino_mega_C_WORLD
    │       │   ├───arduino_mega_D_HELLO
    │       │   ├───arduino_mega_D_U
    │       │   ├───arduino_mega_D_WORLD
    │       │   ├───arduino_mega_X_HELLO
    │       │   ├───arduino_mega_X_U
    │       │   └───arduino_mega_X_WORLD
    │       └───datasets
    │           ├───115200
    │           ├───19200
    │           └───9600
    └───__pycache__
```

There are 3 main folders I2C, SPI, and USART each folder contains a Python script specific to that protocol which is called from the main.py script at the root of the project. Each folder also contains an Arduino receiving script for that specific protocol. Lastly, each folder contains a {protocal}_data folder. This folder contains all the raw waveforms collected and also the feature extracted CSV when the features extraction Python script is run.

The final two folders are the feature extraction folder and the machine learning folder. The feature extraction folder as the name implies deals with feature extraction from the raw waveforms. To use the program run the main.py script and then input the required information. So in this case you will be asked to provide a path to the raw waveforms folder which is usually named {protocal}_data. You will then be asked to specify which protocol is been analyzed and finally, what is the average voltage of the provided waveforms. (AKA 5 volts, 3.3 volts, etc..). The program will then extract the data and output the CSV information inside of the {protocal}_data folder under a new directory called datasets.

The final folder is the machine learning folder this folder only contains one Python script called main.py. This is a simple script that just trains a machine learning model on the USART datasets and performs a prediction on some random feature extract dataset. The program then outputs which board it thinks the data is connected to. This script is the main one that requires the most work since most of the code is currently hard code in this script.

## Questions
Email me at ramon@ramongarciajr.tech
