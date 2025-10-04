
def two_sum(arr,target):
	hash={}
	for i in range(len(arr)):
		if target-arr[i] in hash:
			return [hash[target-arr[i]],i]
			
		else:
			hash[arr[i]]=i
			
	return -1
	
print(two_sum([2,7,11,15],9))
	
	