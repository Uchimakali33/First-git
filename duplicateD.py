def duplicate(arr):
	hash={}
	for i in range(len(arr)):
		if arr[i] in hash:
			hash[arr[i]]+=1
			return True
		else:
			hash[arr[i]]=1
	return True
	
arr=[1,2,3,1]
print(duplicate(arr))
			