import math
def check_snt(n):
    if n<=1:
        return False
    if n ==2:
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if(n%i==0):
                return False
        return True
def find_gcd(a,b):
    if (b==0):
        return a
    else:
        x1 = 0
        x2 = 1
        y1 = 1
        y2 = 0
        while(b>0):
            q = math.floor(a/b)
            r = a - b*q
            x = x2 - x1*q
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
        return (d)
def find():
    dem = 0
    for i in range(1,1000):
        for j in range(i,1000):
            if(check_snt(find_gcd(i,j)) is True):
                dem = dem +1
    print(dem)
find()