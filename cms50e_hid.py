import time
import hid
import csv

'''
This program is used to extract data information from the Contec CMS50E, 
including PPG signals, Heart rate signals, and SPO2 signals.
Before use, you need to determine the hardware ID of the CMS50E after connected to the computer.
'''

# Delay the start time of data collection, ready to start collecting data
def delay_start(delay_time):
    print("Start recording in...")
    for i in range(delay_time):
        print(delay_time - i)
        time.sleep(1)

def collect_data(device, csvFileName):
    # Initialize data
    check_bit = 0
    data_update_bit = 0
    status_bit = 0
    PPG_bit = 0
    HR_bit = 0
    SPO2_bit = 0
    data_count = 0

    with open(csvFileName, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Count', 'Time', 'PPG', 'HR', 'SPO2'])

    delay_start(3)
    start_time = time.time()

    while True:
        data = device.read(18)
        # hex_data = []
        # for i in range(len(data)):
        #     hex_data.append(hex(data[i]))
        # print(hex_data)
        print(data)

        current_time = time.time()
        time_count = current_time - start_time
        if time_count > stop_time:
            break

        # Parse the received data
        for i in range(3):
            check_bit = data[0 + 6*i]
            data_update_bit = data[1 + 6*i]
            status_bit = data[2 + 6*i]

            # while data_update_bit==1, Update HR and SPO2
            if data_update_bit == 0:
                PPG_bit = data[3 + 6*i]
            elif data_update_bit == 1:
                HR_bit = data[3 + 6 * i]
                SPO2_bit = data[4 + 6 * i]

            # Save PPG, HR, SPO2 in csv
            with open(csvFileName, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(data_count), str(PPG_bit), str(HR_bit), str(SPO2_bit)])
            data_count = data_count + 1

if __name__ == '__main__':
    # Parameters
    VENDOR_ID = 0x28E9
    PRODUCT_ID = 0x028A
    SYNC = 0x80
    PULSE = 0x40
    csvPath = 'G:/Project/Fatigue/data/myDataset/test/'
    csvFileName = csvPath + 'Output1' + '.csv'
    stop_time = 120

    device = hid.device()
    device.open(VENDOR_ID, PRODUCT_ID)
    print("Opening the device")

    collect_data(device, csvFileName)

