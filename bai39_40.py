import math
def check_prime(n):
    check = True
    if n == 1: return False
    elif n == 2: return True
    else:
        for i in range(3, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                check = False
                break
    return check
 
def find_gcd(a,b):
    if b==0:
        return a
    else:
        x2=1
        x1=0
        y2=0
        y1=1
        while(b>0):
            q = math.floor(a/b)
            r = a -q*b
            x= x2 -x1*q
            y = y2 - y1*q
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
def main():
    list_num = []
    count = 0
    n = int(input('Nhap vao so phan tu cua mang: '))
    for i in range(n):
        if n > 0:
            a = int(input("Nhap vao phan tu thu {0}: ".format(i+1)))
            list_num.append(a)
        else:
            print("Gia tri phai > 0")
    print(list_num)
    
    for i in range(len(list_num)):
        for j in range(i+1, len(list_num)):
            if check_prime(find_gcd(list_num[i],list_num[j])) is True:
                print(list_num[i], list_num[j], find_gcd(list_num[i],list_num[j]))
                count += 1
                
    print('So cap thoa man: {0}'.format(count))  
    
main()
