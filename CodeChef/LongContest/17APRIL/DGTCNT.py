def isHated(num,hateList):
	count = [0]*10
	n = num
	while num>0:
		rem = num%10
		num = num/10
		count[rem]+=1

	#comment
	for i in str(n):
		if count(int(i)) == hateList(int(i)):
			return True
	
	return False
	# print num,count
	# 	for i in xrange(10):
	# 		if count[i]==hateList[i]:
	# 			return True
 
 
t = int(input())
for idx in xrange(t):
	l,r = map(int,raw_input().strip().split())
	hate = map(int,raw_input().strip().split())
	count = 0
	allZero = True
	for i in hate:
		if i!=0:
			allZero=False
			break
	if allZero:
		count = +1
	else:
		for i in xrange(l,r+1):
			# print i
			if not isHated(i,hate):
				count += 1
			# else:
				# print 'not'
	print count 