import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def find(n):
    list1 = []
    for i in range(0,n):
        if(check_snt(i)==True):
            list1.append(i)
    for i in range(0,len(list1)-3):
        a = list1[i] + list1[i+1] + list1[i+2] + list1[i+3]
        if(a<=n):
            print(list1[i], list1[i+1], list1[i+2], list1[i+3])
n = int(input("Nhap vao so n: "))
find(n)