import numpy as np
import random
from random import randrange
import matplotlib.pyplot as plt

def sign(a):
    if a > 0:
        return 1
    else:
        return -1

file = open("hw1_18_train", mode = "r")
traindata = file.read().strip()
traindata = traindata.replace('\t', ' ')
traindata = traindata.split('\n')
cnt = 0
for line in traindata:
    traindata[cnt] = line.split()
    cnt1 = 0
    for element in traindata[cnt]:
        if cnt1 != 4:
            traindata[cnt][cnt1] = float(element)
        else:
            traindata[cnt][cnt1] = int(element)
        #print(traindata[cnt][cnt1])
        cnt1 += 1
    traindata[cnt] = [traindata[cnt][0], traindata[cnt][1], traindata[cnt][2], traindata[cnt][3], traindata[cnt][4], 1]
    cnt += 1

file1 = open("hw1_18_test", mode = "r")
testdata = file1.read().strip()
testdata = testdata.replace('\t', ' ')
testdata = testdata.split('\n')
cnt2 = 0
for line1 in testdata:
    testdata[cnt2] = line1.split()
    cnt3 = 0
    for element in testdata[cnt2]:
        if cnt3 != 4:
            testdata[cnt2][cnt3] = float(element)
        else:
            testdata[cnt2][cnt3] = int(element)
        #print(testdata[cnt][cnt1])
        cnt3 += 1
    testdata[cnt2] = [testdata[cnt2][0], testdata[cnt2][1], testdata[cnt2][2], testdata[cnt2][3], testdata[cnt2][4], 1]
    cnt2 += 1

tot = 0
arr = np.zeros(1126)
for time1 in range(0, 1126):
    wtrain = np.zeros(5)
    time = 1
    while True:
        index = randrange(len(traindata))
        total = traindata[index][5] * wtrain[4]
        for j in range(0, 4):
            total += wtrain[j] * traindata[index][j]
        if sign(total) != traindata[index][4]:
            time += 1
            for j in range(0, 4):
                wtrain[j] += traindata[index][4] * traindata[index][j]
            wtrain[4] += traindata[index][5] * traindata[index][4]
        if time == 100:
            break
    error1 = 0
    for i in range(0, cnt2):
        total1 = testdata[i][5] * wtrain[4]
        for j in range(0, 4):
            total1 += wtrain[j] * testdata[i][j]
        if sign(total1) != testdata[i][4]:
            error1 += 1
    arr[time1] = error1 / cnt2
    #print(error1 / cnt2)
    tot += error1 / cnt2

plt.xlabel('error rate')
plt.ylabel('frequency')
plt.hist(arr)
plt.show()
averageerror = tot / 1126
print(averageerror)
file.close()
file1.close()