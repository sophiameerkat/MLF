import numpy as np
import random
import matplotlib.pyplot as plt

def sign(a):
    if a > 0:
        return 1
    else:
        return -1

file = open("hw1_15", mode = "r")
data = file.read().strip()
data = data.replace('\t', ' ')
data = data.split('\n')
cnt = 0
tot = 0
for line in data:
    data[cnt] = line.split()
    cnt1 = 0
    for element in data[cnt]:
        if cnt1 != 4:
            data[cnt][cnt1] = float(element)
        else:
            data[cnt][cnt1] = int(float(element))
        #print(data[cnt][cnt1])
        cnt1 += 1
    data[cnt] = [data[cnt][0], data[cnt][1], data[cnt][2], data[cnt][3], data[cnt][4], 1]
    cnt += 1

arr = np.zeros(1126)
for time in range(0, 1126):
    random.shuffle(data)
    w = np.zeros(5)
    flag = 1
    error = 0
    while flag == 1:
        correct = 0
        for i in range(0, cnt):
            total = data[i][5] * w[4]
            for j in range(0, 4):
                total += w[j] * data[i][j]
            if sign(total) != data[i][4]:
                for j in range(0, 4):
                    w[j] += data[i][4] * data[i][j]
                w[4] += data[i][5] * data[i][4]
                error += 1
            else:
                correct += 1
        if correct == cnt:
            flag = 0
    arr[time] = error
    tot += error

plt.xlabel('updates')
plt.ylabel('frequency')
plt.hist(arr)
plt.show()
averageerror = tot / 1126
print(averageerror)
file.close()
