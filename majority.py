def majority(arr):
	hash={}
	n=len(arr)
	for i in range(len(arr)):
		if arr[i] in hash:
			hash[arr[i]]+=1			
		else:
			hash[arr[i]]=1
		if hash[arr[i]]>(n/2):
				majority=arr[i]
			
	return majority
	
print(majority([1]))
	