t=int(input())
j=1
while t:
	n=int(input())
	arr=list(map(int, input().split()))
	count=0
	for i in range(n-1):
		if arr[i]>max(arr[i:]):
			count+=1
		if arr[i+1]<arr[i]:
			count+=1
	print("Case #" + str(j) + " " + str(count))
	j+=1
	t-=1