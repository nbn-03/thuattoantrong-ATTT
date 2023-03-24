import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def find(n,m):
    if(n==0 and m ==0):
        return True
    if (n==0 or m==0):
        return False
    for i in range(2,n+1):
        if(check_snt(i) is True):
            if(find(n-i,m-1) is True):
                print(i,end=' ')
                return True
n  = int(input("nhap so n: "))
m  = int(input("nhap so m: "))
if(find(n,m) is True):
    print("có",m,"gia tri tach ra")