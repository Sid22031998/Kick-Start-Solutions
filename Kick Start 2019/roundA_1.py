t=int(input())
for k in range(1, t+1):
	n,m=list(map(int, input().split()))
	arr=list(map(int, input().split()))
	arr.sort()
	count=10e9
	for i in range(n):
		if m==arr.count(arr[i]):
			count=0
			break
		else:
			c=0
			l=m
			for j in range(n):
				if arr[i]!=arr[j]:
					if l:
						c+=arr[i]-arr[j]
						l-=1
					else:
						break
				else:
					l-=1
			if c>0:
				count=min(c, count)
					
	print("Case #" + str(k) + ": " + str(count))