import math
import random
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
    n = int(input('Nhap vao so tu nhien n: '))
    p, count = 1, 0
    while check_prime(p) is False:
        p = random.randrange(1, 1000, 2)
    if (n>0) and (n<1000):
        for i in range(n):
            if check_prime(nhanbpcl(i, p, n)) is True:
                count += 1
                print('{0}: {1}^{2} mod {3} = {4}'.format(count,i,p,n,nhanbpcl(i, p, n)))
main()