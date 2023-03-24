import math
def check_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def binary(n):
    list = []
    while(n>0):
        a = int(float(n%2))
        list.append(a)
        n = (n-a)/2
    return list
def nhanbpcl(a,k,n):
    list = binary(k)
    b = 1
    if k==0:
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
def main():
    a = int(input('Nhap vao so tu nhien a: '))
    k = int(input('Nhap vao so mu: '))
    n = int(input('Nhap vao so mod: '))
    if  (0 < a < 1000) and (0 < k < 1000) and (0 < n < 1000):
        if check_prime(nhanbpcl(a, k, n)) is True:
            print('La So Nguyen To')
        else:
            print('La Hop so')
main()