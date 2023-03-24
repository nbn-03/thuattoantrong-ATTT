import math
def check_prime(n):
    if n<=1:
        return False
    if n ==2:
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if(n%i==0):
                return False
        return True
def find_k(n):
    ceil = 0
    floor = 0
    for i in range(n,2,-1):
        if(check_prime(i)==True):
            floor = i
    while(True):
        if(check_prime(n)==True):
            ceil = n
            break
        else:
            n = n + 1
    if (ceil - n) < (n - floor):
        return ceil
    else:
        return floor
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
    if k ==0:
        return b
    else:
        A = a
        if(list[0]==1):
            b = a
        for i in range(1,len(list)):
            A = pow(A,2)%n
            if(list[i]==1):
                b = (A*b)%n
            else:
                b = b
        return b
def find(SBD):
    k = find_k(SBD)
    print(nhanbp(SBD,k,123456)) # dùng pow(SBD,k,123456)-hàm hỗ trợ
SBD = int(input("nhap SBD: "))
find(SBD)