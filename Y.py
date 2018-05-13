import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#1
def Sigmoid(x):
    y=1/(1+np.power(np.e,x))
    return y

x=np.arange(-3,3,0.1)
y=Sigmoid(x)

plt.plot(x,y,"r")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

#2 Histogram

m = np.random.randint(0,10,(5,5))
print(m)
print("-----------")
h = np.zeros(10)
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        h[m[i, j]] += 1
print(h)
print("-----------")
print(m[i,j])

#3

def histogramOfImg(m):
    h = np.zeros(10)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            h[m[i,j]]+=1
    return h

m = np.random.randint(0,10,(10,10))
h = histogramOfImg(m)
plt.bar(np.arange(0,10,1),h) #oszlopdiagram
#plt.hist(np.reshape(m,10*10),10)
plt.show()

#4



