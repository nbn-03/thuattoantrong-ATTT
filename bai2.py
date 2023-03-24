import math
def ktsnt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def main():
    a = int(input('Nhap vao so n: '))
    for i in range(pow(10,a-1),pow(10,a)):
        if(ktsnt(i)==True):
            print(i)
main()