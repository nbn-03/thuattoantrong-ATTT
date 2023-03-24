import math
def check_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if(n%i==0):
                return False
    return True
def find_gcd(a,b):
    if b==0:
        return a
    else:
        x2 = 1
        x1 = 0
        y2 = 0 
        y1 = 1
        while(b>0):
            q = math.floor(a/b)
            r = a - q*b
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
        return (d)
def binary(n):
    list = []
    while(n>0):
        a = int(float(n%2)) # Tinh phan du
        list.append(a) # Day phan du vao danh sach
        n = (n-a)/2 # Tinh phan thuong cho phep tinh tiep theo
    return list 
def nhanbp(a,k,n):
    list = binary(k)
    b = 1 
    if k==0:
        return b 
    else:
        A = a
        if list[0]==1:
            b = a
        for i in range(1,len(list)):
            A = pow(A,2) % n
            if list[i]==1:
                b = (A*b) % n
            else:
                b = b
        return b
def fermat(n):
    for b in range(2,n):
        if(find_gcd(b,n)==1):
            if(nhanbp(b,n-1,n)!=1):
                return False
    return True
def iscarmichael(n):
    dem = 0
    for i in range(2,n):
        if(check_prime(i)==False):
            if(fermat(i)==True):
                dem = dem +1
    print(dem)
n = int(input("nhap so n: "))
iscarmichael(n)