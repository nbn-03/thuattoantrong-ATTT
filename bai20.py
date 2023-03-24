import math
def find_gcd(a,b):
    if(b==0):
        return a
    else:
        x2 = 1 
        x1 = 0
        y2 = 0
        y1 = 1
        while(b>0):
            q = math.floor(a/b)
            r = a-q*b
            x = x2 - q*x1
            y = y2 - q*y1
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
            d = a
            x = x2
            y = y2
        return(d)
def find(m,n,d):
    for i in range(m+1,n):
        for j in range(i+1,n):
            if(find_gcd(i,j)==d):
                print(i,j)
m = int(input('m: '))
n = int(input('n: '))
d = int(input('Nhap vao gia tri d cho truoc: '))
find(m,n,d)