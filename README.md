# Contec CMS50E PPG dataloader

## Introduction

Receive serial port data from Contec CMS50E in real time through HID interface, obtain PPG raw signal, heart rate, SPO2 data, and save it. You can use the raw PPG signal to perform further data analysis, including comparing the accuracy of rPPG algorithms, training deep learning networks, and more.

Contec CMS50E oximeter

<img src="https://github.com/SunHaixin0324/CMS50E_PPG_loader/blob/master/figures/oximeter.jpg" style="zoom:50%;" /> 

## Usage

1. Install python3 and the corresponding pip program。

2. Install hidapi by entering in a shell : `pip3 install hidapi`

3. Start the Smart Device Assistant software on your computer (It can usually be installed through the U disk included in the box of the oximeter or obtained by consulting customer service).

   <img src="https://github.com/SunHaixin0324/CMS50E_PPG_loader/blob/master/figures/Smart%20Device%20Assistant.PNG" style="zoom:50%;" /> 

4. Put your finger on the oximeter, turn it on, and plug it into the computer. Make sure it works well, that is, you can see the curve change on your computer software before moving on to the next step.

5. Check the hardware id of your oximeter in Device Manager (my device is *VENDOR_ID = 0x28E9*, *PRODUCT_ID = 0x028A*). Modify the PPG file storage path in the program to ensure that data can be stored correctly.

6.  Run the script `cms50e_hid.py` to load data and save as csv file.

## Specification

- The code works both for Windows and Ubuntu
- The Sampling frequency of the device is 60Hz
- The oximeter sends 60 data per second to the PC, each data contains 6 bytes, and different data is separated by `0xeb`.
- When the second byte is 0, the oximeter is in the stage of collecting PPG signal, and the fourth byte of data at this time is the PPG signal; When the second byte is 1, the oximeter is in the updating data display stage, at this time the fourth byte of data is the heart rate value, and the fifth byte of data is SPO2. The data is updated approximately once per second.

## Result

Waveform of collected PPG signal (first 10s)

<img src="https://github.com/SunHaixin0324/CMS50E_PPG_loader/blob/master/figures/PPG%20waveform.PNG" style="zoom:50%;" /> 