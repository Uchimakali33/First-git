def find_unique(arr):
	hash={}
	unique=-1
	for i in range(len(arr)):
		element=arr[i]
		
		if element in hash:
			hash[element]+=1
		else:
			hash[element]=1
	print(hash)		
	for i in hash:
		if hash[i]==1:
			unique=i
	return unique
	
print(find_unique([2,1,2]))
			
		