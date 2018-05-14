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

def gcd(a,b):
    if b > a:
        return gcd(b,a) #16,12 #12,4
    r = a%b
    if r == 0:
        return b
    return gcd(r,b) #4 #12


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

print(gcd(12,16))
print(lcm(12,16))

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

import numpy

def sortByCol(v,ind):
    for i in range(v.shape[0]):
        for j in range(i+1,v.shape[0]):
            if v[i][ind]>v[j][ind]: #sor,oszlop
                v[i][ind],v[j][ind]=v[j][ind],v[i][ind]

v=np.random.randint(1,100,(4,5))
print(v)
ind=int(input("oszlop: "))
sortByCol(v,ind)
print(v)

#19

def sortByRow(v,ind):
    for i in range(v.shape[1]):
        for j in range(i+1,v.shape[1]):
            if v[ind][i]>v[ind][j]: #sor,oszlop
                v[ind][i],v[ind][j]=v[ind][j],v[ind][i]

v=np.random.randint(10,50,(4,5))
print(v)
ind=int(input("sor: "))
sortByRow(v,ind)
print(v)

#20

import numpy as np

m = np.random.randint(1,5,(3,4))
print(m)
colSum = m.sum(axis=0) #oszlop axis=0
rowSum = m.sum(axis=1) #sor axis=1
print(colSum)
print(rowSum)

#21

import numpy as np

m = np.random.randint(1,2,(3,3))
print(m)
colSum = m.sum(axis=0)
print(colSum)
print(np.sum(colSum==colSum[0]))
print(colSum.size)
if colSum.size==(np.sum(colSum==colSum[0])):
    print(True)
else:
    print(False)

#22

def rowColSum(x):
    print(x)
    colSum = x.sum(axis=0)
    rowSum = x.sum(axis=1)
    return np.sum(colSum == colSum[0]) + np.sum(rowSum == colSum[0]) == colSum.size + rowSum.size

m=np.ones((5,5))
n=np.random.randint(1,100,(5,5))
print(rowColSum(m))
print(rowColSum(n))

#22/b

def isRowColSumEq(m):
    print(m)
    colSum=m.sum(axis=0)
    rowSum=m.sum(axis=1)
    return np.sum(colSum==colSum[0])+np.sum(rowSum==rowSum[0])==colSum.size+rowSum.size

m=np.ones((4,4))
print(isRowColSumEq(m))
n=np.random.randint(1,3,(2,2))
print(isRowColSumEq(n))

#23

import numpy as np

m=np.random.randint(1,50,(4,5))
print(m)
print("-------------------")
print(m.shape)
for i in range(0,m.shape[1]):
    for j in range(0,m.shape[0]):
        x=(m[:,2]) #sor oszlop
        y=(m[j,i])
print("-------------------")
print(x)
print(y)

#24

import numpy as np

m=np.random.randint(1,3,(3,3))
print(m)
print("-------------")
print(m[:,:]>1)
print("-------------")
for i in range(m.shape[1]):
    print(m[:,i])
print("-------------")
print(m[:,2])
print("-------------")
for i in range(m.shape[1]):
    print(m[:,i] > 1)

#25

import numpy as np

def indicesCol(m):
    L=[]
    for i in range(0,m.shape[1]):
        if np.sum(m[:,i]==0)>0:
            if np.sum(m[:,i]==0)*2<=np.sum(m[:,i]<0):
                L.append(i)
    return L

str = input('Give the shape of array:')
n,m = str.split(',')
m = np.random.randint(-1,1,(int(n),int(m)))
print(m)
print(indicesCol(m))

#26

import numpy as np

m=np.random.randint(0,2,(4,4))
print(m)
print("---")
for i in range(m.shape[0]):
    print(np.sum(m[i, :] == 0))
print("---")
for i in range(m.shape[0]):
    print(np.sum(m[i, :] > 0))
print("---")
x=[] #annak a sornak az indexe, amiben megegyezik a 0-k és 1-ek száma
for i in range(m.shape[0]):
    if np.sum(m[i, :] == 0) == np.sum(m[i, :] > 0):
        x.append(i)
print(x)

#27

import numpy as np

def listOfSpecialElements(m): #Elemek+idx - eredeti indexükkel oszthatóak
    L=[]
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i,j]%(i+1)==0 and m[i,j]%(j+1)==0:
                L.append((m[i,j],i,j))
    return L

m = np.random.randint(10,45,(4,5))
print(m)
print('--------------')
print(listOfSpecialElements(m))

#28 DICTIONARIES

dict={"Bob":"dog", "Henry":"cat", "Thomas":"lamb"}
print(dict)
print(dict["Bob"]) #dog
print(len(dict)) #3 key-value párok egynek számítanak

print("Henry" in dict) #Key-in dict - True
print("cat" in dict) #Value - False

a=dict
print(a)

for key in dict:
    print(key,"is a",dict[key]) #k-key

dict2={v:k for k,v in dict.items()}
print(dict2)

#29

L=[]
str=open("input.txt","r")
for i in str:
    L.append(i)
print(L[2]) #3.sor

#30

def clearRow(str):
    newR=""
    for ch in str:
        if ch not in string.punctuation and ch!="\n":
            newR+=ch.lower()
    return newR

fin=open("input.txt","r")
dict={}
for row in fin:
    crow=clearRow(row)
    for word in crow.split(" "):
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
for k in dict:
    print(k,":",dict[k])

L1=[]
L2=[]
for i in dict:
    L1.append(dict[i]) #values
    L2.append(i) #keys
max=max(L1)
idx=0
while L1[idx]!=max:
    idx+=1
print("The word that occurs the most is:",L2[idx])


#31

L1=[]
L2=[]
for i in dict:
    L1.append(dict[i]) #values
    L2.append(i) #keys
lw=L2[0]
for i in range(len(L2)):
    if len(L2[i])>len(lw):
        lw=L2[i]

idx=0
while L2[idx]!=lw:
    idx+=1

print("The longest word in dictionary is '{}' and its indice is: {}".format(lw,idx))

#32

month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
nums=range(1,13)
Dict=dict(zip(month,nums))
print(Dict)

#33

D_Months={"JAN":1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEP":9, "OCT":10, "NOV":11, "DEC":12}
#8-MAR-85
def dateConv(string):
    st=string.split("-")
    if int(st[2])<19:
        year="20"+st[2]
    else:
        year="19"+st[2]
    return (int(year),D_Months[st[1]],int(st[0]))

str = input("Give me a date in format (dd-MMM-yy): ")
print(dateConv(str))

#34

dict={}
dict[1]=[7,8]#lista - value
print(dict)
if 1 in dict:
    dict[1].append(9)
print(dict)

#35

dict={}
for d1 in range(1,7):
    for d2 in range(1,7):
        if d1+d2 in dict:
            dict[d1+d2].append((d1,d2))
        else:
            dict[d1+d2]=[(d1,d2)]

for k,v in dict.items():
    print(k,":",v)

#36 SETS

my_set={'a','b','c','c','c'} #nincs ism., nem rendezett
my_set2={'a',1,3.12145,True}

print(my_set)
#print(my_set2)

print(len(my_set)) #3

for element in my_set:
    if element=='b':
        print(True)
    print(False)
print("----------")
print("q" in my_set) #false
print("c" in my_set) #true

#37

a_set=set("abcd")
print(a_set)
b_set=set("cdef")
print(b_set)

print("intersection:",a_set & b_set)

print("difference:",a_set - b_set)

print("union:",a_set | b_set)

print("symmetric difference:",a_set ^ b_set)

small_set=set("abc")
big_set=set("abcdef")

print(small_set<=big_set) #részhalmaz
print(small_set>=big_set)

#38

a_set=set("abcd")
print(a_set)
b_set=set("cdef")
print(b_set)

a_set.add("x")
print(a_set)

b_set.clear()
print(b_set)

a_set.remove("a") #a_set.discar("a") ugyanaz, de nincs hiba, ha nincs elem
print(a_set)

print(a_set.copy())

#39

a_set=set("abcdefghulu")

def remover(set,word):
    for i in word:
        if i in set:
            set.remove(i)
    return set

print(a_set)
print(remover(a_set,"hulu"))

#40

a=set("abc")
b=set("abcdef")
print(b.issuperset(a))
print(a.issubset(b))

#41

a={1,2,3,4}
a.update({5,6,7,"str"},"str")
a.add("x") #csak egy
a.add(666)
print(a)

#42

import random

wheel=set(range(0,37))
wheel.add("00")

odd=set(range(1,37,2))
even=set(range(2,37,2))
reds={1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
blacks=wheel-reds
lower=set(range(1,19))
higher=set(range(19,37))

sets={"even":even,"odd":odd,"reds":reds,"blacks":blacks,"lower":lower,"higher":higher}

num=random.choice(list(wheel))

for s in sets:
    if num in sets[s]:
        print("The number {} is {}".format(num,s))