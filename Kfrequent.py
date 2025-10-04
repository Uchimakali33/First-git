hash={}

def frequent(arr,k):
	for i in range(len(arr)):
		if arr[i] not in hash:
			hash[arr[i]]=1
		else:
			hash[arr[i]]+=1
	print(hash.items())
	print(hash)
arr=[1,2,1,3,2]
k=2
print(frequent(arr,k))

	
	
	