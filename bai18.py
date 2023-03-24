import math
W = 8
p = 2147483647
m = math.ceil(math.log2(p))
t = math.ceil(m/W)
list1 = []
list2 = []
list3 = []
def find_array(n,t):
    list = []
    for i in range(t-1,-1,-1):
        list.append(n // pow(2,i*W))
        n = n % pow(2,i*W)
    return list
def find_sum(a,b):
    list1 = find_array(a,t)
    list2 = find_array(b,t)
    e = 0
    sum = 0
    for i in range (t-1,-1,-1):
        sum=(list1[i]+list2[i]+e)
        if (sum>=0 and sum<pow(2,W)):
            list3.append(sum%pow(2,W))
            e = 0
        else:
            list3.append(sum%pow(2,W))
            e = 1
    list3.reverse() 
    print(e,list3)
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
find_sum(a,b)