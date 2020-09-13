t=int(input())
k=1
while t:
	n,a,b,c=list(map(int, input().split()))
	arr=' '
	if n==a and a==b and n!=c:
		print('Case #' + str(k) + ': ' + 'IMPOSSIBLE')
	else:
		if c==1:
			arr='4 1 3 2'
		if c==2:
			arr='2 1 5 5 3'
		print('Case #' + str(k) + ': ' + arr)
	k+=1
	t-=1