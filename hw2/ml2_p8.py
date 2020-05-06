import numpy as np 
import random
import matplotlib.pyplot as plt 

noise = 0.2

def sign(a):
	if a > 0:
		return 1
	else:
		return -1

def f_function(x, pro):
	if pro >= noise:
		return sign(x)
	else:
		return -sign(x)

def h_function(s, x, theta):
	return s * sign(x - theta)

def generate_x(X):
	for i in range(0, 20):
		x = random.uniform(-1, 1)
		X.append(x)

def generate_y(Y):
	for x in X:
		pro = random.uniform(0, 1)
		Y.append(f_function(x, pro))

def generate_theta(FirstTheta, Theta):
	l = len(FirstTheta)
	for i in range(l):
		if i == 0:
			Theta.append((FirstTheta[0] - 1) / 2)
		else: 
			Theta.append((FirstTheta[i] + FirstTheta[i - 1]) / 2)

def cal_Eout(s, theta):
	return 0.5 + 0.3 * s * (abs(theta) - 1)

ans = []
totEin = 0
totEout = 0
totminus = 0

for i in range(0, 1000):
	X = []
	Y = []
	FirstTheta = []
	Theta = []
	generate_x(X)
	generate_y(Y)
	FirstTheta = np.sort(X)
	generate_theta(FirstTheta, Theta)
	Ein = 10000000

	for theta in Theta:
		for s in [-1, 1]:
			e = 0
			length = len(X)
			for index in range(length):
				result = h_function(s, X[index], theta)
				if result * Y[index] == -1:
					e += 1
			curerror = e / length
			if curerror < Ein:
				Ein = curerror
				choose_s = s
				choose_theta = theta

	Eout = cal_Eout(choose_s, choose_theta)
	totEin += Ein
	totEout += Eout
	totminus += Ein - Eout
	ans.append(Ein - Eout)

#print(totEin / 1000)
#rint(totEout / 1000)
#print(totminus / 1000)
plt.xlabel('Ein - Eout')
plt.ylabel('frequency')
plt.hist(ans, bins = 90)
plt.show()