t=int(input())
k=1
while t:
	n=int(input())
	arr=[1]*n
	brr=list(map(int, input().split()))
	j=-1
	d=0
	for i in range(1,n):
		c=brr[i]-brr[i-1]
		if c==d:
			arr[j]+=1
		else:
			j+=1
			arr[j]+=1
			d=c
	print('Case #' + str(k) + ': ' + str(max(arr)))
	k+=1
	t-=1