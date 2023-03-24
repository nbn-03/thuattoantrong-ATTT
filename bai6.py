import math
def uoc(n):
    a = 0
    for i in range (1,n):
        if(n%i==0):
           a = a + i
    return a
def kt(n):
    list = []
    for i in range (2,n):
        for j in range (i+1, n):
            if(uoc(i)==j and uoc(j)==i):
                list.append(i)
                list.append(j)
    print(list)
n = int(input('Nhap vao so n: '))
kt(n)