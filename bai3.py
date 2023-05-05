def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c

def giaipt(a,b,c):
    d=b**2-4*a*c
    if d<0:
        x1=x2=[0]
        print("Phuong trinh vo nghiem")
    elif d==0:
        x1=x2=-b/(2*a)
        print('Phuong trinh co nghiem kep')
    elif d>0:
        x1=(-b+d**0.5)/2*a
        x2=(-b-d**0.5)/2*a
        print("Phuong trinh co 2 nghiem")
    return x1,x2,d

def inkq(x1, x2,d):
    if d>0:
        print("x1=", x1,sep="")
        print("x2=", x2,sep="")
    if d==0:
        print("x1=x2=",x1,sep='')

a,b,c = nhap()
x1,x2,d = giaipt(a,b,c)
inkq(x1, x2,d)
