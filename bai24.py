import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def find_array(b):
    list = []
    for i in range (0,int(math.sqrt(b))+1):
        list.append(pow(i,2))
    return list
def find(a,b):
    #dem = 0
    s1 = find_array(b)
    s2 = find_array(b)
    for i in range(a,b+1):
        if(check_snt(i)==True):
            for j in range(0,len(s1)):
                for k in range(j,len(s2)):
                    if(s1[j]+s2[k]==i):
                        #dem = dem +1
                        print(i)
    #print(dem)
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
find(a,b)