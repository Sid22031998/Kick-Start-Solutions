n=int(input())
j=1
while n:
    a,b=list(map(int, input().split()))
    arr=list(map(int, input().split()))
    arr.sort()
    c=0
    for i in arr:
        if b-i<=0:
            break
        c+=1
        if b>=i:
            b=b-i
    print("Case #" + str(j) + ": " + str(c))
    j+=1  
    n-=1