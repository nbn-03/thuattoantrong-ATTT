def lastOccurrence(p,T):# Hàm tìm vị trí của các phần tử của T trong p nếu có nhiều vị trí thì lấy ở cuối
    x = list(set(T))# lấy những phần tử khác nhau trong T
    x.sort() 
    f = [] # mảng chứa vị trí nếu x[i] mà có trong p thì f[i] chứa vị trí của x[i] còn ko thì f[i]=-1
    for i in range(len(x)):#Duyệt các phần tử trong x
        vt=-1
        for j in range(len(p)-1,-1,-1): # Duyệt các phàn tử trong p
            if p[j]==x[i]: # Nếu tìm thấy x[i] trong p
                vt = j
                break
        f.append(vt)
    return x,f
def Boyer_Moore(p,T):
    x,f = lastOccurrence(p,T) # x: chứa chữ cái trong T, f chứa vị trí của những chữ cái đó trong p
    L = dict(zip(x,f))# gộp x và f thanh dict có dạng {x[i]:f[i]}
    # phần dưới như trong thuật toán
    i = len(p)-1
    j = len(p)-1
    while(i<len(T)):
        while (j>=0) and (T[i]==p[j]): 
            i-=1
            j-=1
        if (j==-1): 
            return i+1
        else: 
            i = i+len(p)-min(j,1+L[T[i]])
            j = len(p)-1
    return -1
p = input("nhap p: ")
T = input("nhap T: ")
print(Boyer_Moore(p,T))
