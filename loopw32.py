n=int(input('n='))
while n>50 or n<1:
    print('Moi nhap lai')
    n=int(input("n="))
k=1
i=0
while i<=n//10:
    j=1
    while j<=10:
        if k<=n:
            print(k,end=" ")
            k+=1
        else:
            break
        j+=1
    print()
    i+=1
