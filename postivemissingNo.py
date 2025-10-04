def positiveMissingNo(arr):
	hash=set(arr
	
	n=len(arr)
	for i in range(1,n+1):
		if i not in hash:
			missing=i
	return missing	
print(positiveMissingNo([3,4,-1,1]))