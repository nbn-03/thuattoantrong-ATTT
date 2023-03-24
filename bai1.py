import math
def q_prime(n):
    list_q_prime = []
    for i in range(1,n+1):     
        count = 2
        for j in range (2, i):
            if (i % j == 0):
                count += 1
        if count == 4:
            list_q_prime.append(i)       
    print(list_q_prime)
def main():
    n = int(input('Nhap vao so n: '))
    q_prime(n)    
main()