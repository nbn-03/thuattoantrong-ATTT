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
    for i in range(0,n):
        for j in range(0,i+1):
            if(check_snt(j) is True):
                if(i%j==0 and i%pow(j,2)==0):
                    print(i,j)
n = int(input("nhap so n: "))
find(n)