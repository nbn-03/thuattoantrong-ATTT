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
    list = []
    for i in range(0,n+1):
        if(check_snt(i)==True):
            list.append(i)
    for i in range(0,len(list)):
        for j in range(i,len(list)):
            if((check_snt(list[i]+list[j]))==True and check_snt(int(math.fabs(list[i]-list[j])))==True):
                print(list[i],list[j])
n = int(input("Nhap vao so n: "))
find(n)