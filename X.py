#1

def legnOszto(n):
    x=n-1
    while n%x!=0:
        x-=1
    return x

n=int(input("n: "))
while n!=0:
    print(legnOszto(n))
    n=int(input("n: "))

#2

a=12
b=16

def gcd(a,b):
    if b > a:
        return gcd(b,a) #16,12 #12,4
    r = a%b
    if r == 0:
        return b
    return gcd(r,b) #4 #12

print(gcd(a,b))

#3

while True:
    try:
        i=int(input("n:"))
        print(i)
        i = int(input("n:"))
    except ValueError:
        print("wrong")

#4

try:
    myFile=open("input.txt","r")
    for i in myFile:
        print(i)
    myFile.close()
except FileNotFoundError:
    print("Not found")

#5

def numOfLan(myFile):
    sum=0
    for i in myFile:
        if "Lannister" in i:
            sum+=1
    return sum

try:
    myFile=open("input.txt","r")
    print("The word Lannister occurs",numOfLan(myFile),"times in text.")
    myFile.close()
except FileNotFoundError:
    print("Not found")

#6

def outputer(str):
    newStr=""
    for ch in str:
        if ch.isupper():
            newStr+=ch.lower()
        if ch.islower():
            newStr+=ch.upper()
        else:
            newStr+=ch
    return newStr

try:
    inFile=open("input.txt","r")
    outFile=open("output.txt","w")
    for i in inFile:
        print(outputer(i),file=outFile)
    inFile.close()
    outFile.close()
except FileNotFoundError:
    print("wrong")

#7

import numpy as np

x=np.arange(1,6)
print(x)
print(x.size) #5
print(x[x.size-1]) #5

#8

import numpy as np

def inverseVector(v):
    b=np.array(v[v.size-1])
    for i in range(v.size-2,-1,-1): #hátulról második elemtől 0-ig, visszafele
        b=np.append(b,v[i])
    return b

v=np.arange(1,6)
print(v.size)
print(v)
print(inverseVector(v))

#9

import numpy as np

v=np.random.randint(1,100,5)
print(v)
print(v.max())
print(v.min())
ind=np.where(v==v.max())
ind2=np.where((v==v.min()))
print(ind,ind2)

#10

import numpy as np

x=np.random.randint(1,10,5)
x[x==x.max()]=-1
print(x)

#11

import numpy as np

def sortVector(v):
    n=v.size
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i]>v[j]:
                v[i],v[j]=v[j],v[i]
    return v

v=np.random.randint(1,10,5)
print(v)
print(sortVector(v))

#12

