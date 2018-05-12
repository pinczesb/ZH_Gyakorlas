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

import numpy as np

v=np.arange(1,20)
print(v)
v[(v<8) & (v>2)]=-1
print(v)

#13

import numpy as np

q=np.arange(1,100)
q[(q>5) & (q<50)]=-1
q[q==q.max()]=555
q[q==q.min()]=555
print(q)

#14

n=int(input("n: "))
v=np.random.randint(1,100,5)
print(v)
e=np.abs(v-n)
print(e)
print(v[e==e.min()])

#15

import numpy as np

v=np.random.randint(-10,10,10)
print(v)
sum0=0
for i in v:
    if i==0:
        sum0+=1
sumneg=0
for j in v:
    if j<0:
        sumneg+=1

#16

def sortVector(v):
    n=v.size
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i]>v[j]:
                v[i],v[j]=v[j],v[i]
    return v

e = np.random.randint(1,50,1500)
print(e)
start = t.time()
e1 = sortVector(e)
ended = t.time()
print(e1)
print('{:.3f}'.format(ended-start))

#17

v=np.random.randint(1,100,10)
print(v)

def isSorted(v):
    c=1
    for i in range(0,v.size):
        for j in range(i+1,v.size):
            if v[i]<=v[j]:
                c=c+1
        if c==v.size:
            return True
        return False

def sortVector(v):
    n=v.size
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i]>v[j]:
                v[i],v[j]=v[j],v[i]
    return v

print(isSorted(v))
v2=sortVector(v)
print(v2)
print(isSorted(v2))

#18

