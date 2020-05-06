import numpy as np
import random
import matplotlib.pyplot as plt 

def preprocess(filename):
	d = np.genfromtxt(filename)
	X = d[:, :-1]
	num = d.shape[0]
	X = np.c_[np.ones(num), X]
	Y = d[:, -1].reshape(-1, 1)
	return X, Y

def sigmoid(s):
	return 1 / (1 + np.exp(-s))

def calg(trax, tray, w):
	theta = sigmoid(-np.dot(trax, w) * tray)
	multi = -trax * tray
	tmpg = np.mean(theta * multi, axis = 0)
	g = tmpg.reshape(-1, 1)
	return g

Ein = []
Eins = []

def cal(trax, tray, tesx, texy):
	w = np.zeros((len(trax[0]), 1))
	for i in range(2000):
		g = calg(trax, tray, w)
		w = w - 0.01 * g
		Ytrain_label = np.dot(trax, w)
		Ytrain_label[Ytrain_label > 0] = 1
		Ytrain_label[Ytrain_label <= 0] = -1
		ein = np.mean(Ytrain_label != tray)
		Ein.append(ein)
	#print(ein)

def cals(trax, tray, tesx, texy):
	w = np.zeros((len(trax[0]), 1))
	cnt = 0
	for i in range(2000):
		tmpx = trax[cnt, :]
		x = tmpx.reshape(1, -1)
		g = calg(x, tray[cnt], w)
		w = w - 0.001 * g
		cnt = cnt + 1
		cnt = cnt % trax.shape[0]
		Ytrain_label = np.dot(trax, w)
		Ytrain_label[Ytrain_label > 0] = 1
		Ytrain_label[Ytrain_label <= 0] = -1
		ein = np.mean(Ytrain_label != tray)
		Eins.append(ein)
	#print(ein)

trax, tray = preprocess('hw3_train.dat')
tesx, tesy = preprocess('hw3_test.dat')
cal(trax, tray, tesx, tesy)
cals(trax, tray, tesx, tesy)
plt.plot(Ein, color = 'violet')
plt.plot(Eins, color = 'lightgreen')
plt.xlabel('t')
plt.ylabel('Ein')
plt.show()