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