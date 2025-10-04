def indexOfArray(arr,tar):
	hash={}
	
	for i,num in enumerate(arr):
		if num in hash:
			hash[num].append(i)
			
		else:
			hash[num]=[i]
			
	if tar in hash and len(hash[tar])>1:
		return [hash[tar][0],hash[tar][-1]]
	elif tar in hash and len(hash[tar])==1:
		return [hash[tar][0],hash[tar][0]]
	else:
		return [-1,-1]
		
print(indexOfArray([3,3,3],3))