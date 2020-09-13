from collections import Counter

def canMakePalindrom(s):
    return sum(v % 2 == 1 for v in Counter(s).values()) <= 1

t=int(input())
for k in range(1, t+1):
	n,m=list(map(int, input().split()))
	s=input()
	count=0
	while m:
		l,r=list(map(int, input().split()))
		s1=s[l-1:r]
		if canMakePalindrom(s1):
			count+=1
		m-=1
	print("Case #" + str(k) + ": " + str(count))