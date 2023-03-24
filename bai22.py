import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def check_f(n):
    if(check_snt(n)==True):
        return n
    return 0
def main():
    print('Nhap vao khoang [L, R]: ')
    l = int(input("Nhap vao gia tri L: "))
    r = int(input('Nhap vao gia tri R: '))
    sum = 0
    if 0<l<=10000 and 0<=r<=10000 and r>l:
        for i in range(l, r+1):
            for j in range(i+1, r+1):
                sum += check_f(i) * check_f(j)
main()