import math
import random
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
def Mb(n):
    d = n-1
    r = 0
    while(d%2==0):
        d = d//2
        r = r +1
    for i in range(0,5):
        a = random.randint(2,n-2)
        y = nhanbpcl(a,d,n)
        if(y!=1 and y!=n-1):# n là số nguyên tố a^r đồng dư 1 mod n hoặc a^((2^j)*r) đồng dư với -1 mod n với j nào đó 0<=j<=s-1 
            j = 1
            while(j<=r-1 and y!=n-1):
                y = pow(y,2)%n
                if(y==1):#((a^r)^2j) đồng dư với 1 mà ((a^r)^2j-1) không đồng dư với trừ 1 suy ra gcd(((a^r)^2j-1),n) là thừa số không tầm thường của n (n là hợp số)
                    #thừa sô không tầm thường là ước của n mà ước khác 1 và n
                    return False
                j = j+1
            if (y!=n-1):#a là bằng chứng mạnh chứng tỏ n là hợp số
                return False
    return True
def check_prime(n):
    if(n<=1 or (n%2==0 and n!=2)):
        return False
    if(n==2 or n==3):
        return True
    if(n>=4):
        if(Mb(n) is True):
            return True
        else:
            return False
def main():
    A = []
    B = []
    n = int(input("nhap do dai mang A: "))
    for i in range(0,n):
        a = int(input("nhap mang: "))
        A.append(a)
    for i in range(0,len(A)):
        if(check_prime(A[i]) is True):
            B.append(A[i])
    print(B)
    sum = max(B)
    a = 0
    b = 0
    for i in range(0,len(B)):
        for j in range(i+1,len(B)):
            if(sum>int(math.fabs(B[i]-B[j]))):
                sum = int(math.fabs(B[i]-B[j]))
                a = B[i]
                b = B[j]
    print(sum)
    print(a, b)
main()