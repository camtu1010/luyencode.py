def nhap():
    print ("Nhap 3 so nguyen:")
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    return a,b,c
def max3(a,b,c):
    if a>b and a>c :
        return a
    if b>a and b>c:
     return b
    else:
        return c
def inkq():
    print("So lon nhat la:",tinh )
a,b,c=nhap()
tinh=max3(a,b,c)
inkq() 

   

   

