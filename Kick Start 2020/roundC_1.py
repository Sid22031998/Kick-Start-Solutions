t=int(input())
for k in range(1, t+1):
	n,m=list(map(int, input().split()))
	arr=list(map(int, input().split()))
	count=0
	for i in range(n):
		if arr[i]==m:
			d=m
			for j in range(i, i+m):
				if arr[j]==d:
					d-=1
				else:
					break
			if d==0:
				count+=1
				i=i+m-1
	
	print("Case #" + str(k) + ": " + str(count))