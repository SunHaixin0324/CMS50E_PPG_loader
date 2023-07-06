import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PPG_path = 'G:/Project/Fatigue/data/myDataset/test/Output1.csv'

data = pd.read_csv(PPG_path)
Count = data['Count']
PPG = data['PPG']

PPG = PPG[:600]
PPG_xlabel = np.linspace(0, len(PPG)-1, len(PPG))

plt.title('PPG signal export')
# plt.plot(err_abs_list_minute, 'g^')
plt.plot(PPG_xlabel, PPG, color='orange', label='PPG_wave')
plt.legend()
plt.xlabel('Time(s)')
plt.ylabel('PPG')
plt.show()