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
    p, q, a, count = 1, 1, 1, 0
    while check_prime(q) is False and check_prime(p) is False:
        p = int(random.randrange(1, 1000, 2))
        q = int(random.randrange(1, 1000, 2))
    for a in range(1, 100):
        if check_prime(nhanbpcl(a, p, q)) is True:
            count += 1
            print('{0}: {1}^{2} mod {3} = {4}'.format(count, a, p, q, nhanbpcl(a, p, q)))
    print("So cap thoa man: " + str(count))
main()