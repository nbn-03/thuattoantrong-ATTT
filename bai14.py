import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def reverse(n):
    list = []
    while(n>0):
        list.append(n%10)
        n = n // 10
    num = 0
    for i in range(len(list),0,-1):
        num = num + list[len(list)-i]*pow(10,i-1)
    return num
def find():
    for i in range(100,1000):
        if(check_snt(i)==True):
            for j in range(0,reverse(i)):
                if(pow(j,3)==reverse(i)):
                    print(i)
find()