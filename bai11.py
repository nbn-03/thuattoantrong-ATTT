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
    sum = 0
    for i in range(2,n+1):
        if(check_snt(i)==True):
            sum = sum +i
    return(sum)
n = int(input("Nhap vao so n: "))
print(find(n))
