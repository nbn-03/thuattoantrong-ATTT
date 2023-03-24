import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def check(a,b):
    sum = 0
    for i in range(a,b+1):
        if(check_snt(i)==True):
            sum = sum +i
    if (check_snt(sum)==True):
        print("YES")
    else:
        print("NO")
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
check(a,b)