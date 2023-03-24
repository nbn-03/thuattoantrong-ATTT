import math
import random
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def find(n):
    list = []
    for i in range(0,n):
        list.append(random.randint(0,1000))
    for i in range(0,len(list)):
        if(check_snt(list[i])==True):
            print(list[i])
n = int(input("Nhap vao so n: "))
find(n)