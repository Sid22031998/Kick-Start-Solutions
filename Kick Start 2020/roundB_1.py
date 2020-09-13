t=int(input())
for i in range(1, t+1):
	n=int(input())
	arr=list(map(int, input().split()))
	count=0
	for j in range(1, n-1):
		if arr[j]>arr[j-1] and arr[j]>arr[j+1]:
			count+=1
	print("Case #" + str(i) + ": " + str(count))