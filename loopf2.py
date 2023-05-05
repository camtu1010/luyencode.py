n=int(input("n="))
for i in range(1,n+1):
    print(i, end=' ')
    if i%10==0 or i==n:
        print()
        if i==n:
            break
        print(i+1,end=' ')