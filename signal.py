import serial
import time


# 'COM3' 부분에 환경에 맞는 포트 입력
ser = serial.Serial("COM3", 115200)

signal1 = []
signal2 = []
i = 0
while i < 1000:
    if ser.readable():
        val = ser.readline()

        # print(val)
        print(val.decode()[: len(val) - 1])  # 넘어온 데이터 중 마지막 개행문자 제외

        data = val.decode()[: len(val) - 1]

        signal1.append(data.split(' ')[0])
        signal2.append(data.split(' ')[1])
        i += 1

import matplotlib.pyplot as plt

plt.plot(signal1)
plt.plot(signal2)

plt.show()