def two_sum(arr,target):
	left=0
	right=len(arr)-1
	res=-1
	while left<right:
		if arr[left]+arr[right]>target:
			right-=1
		elif arr[left]+arr[right]<target:
			left+=1
			
		else:
			res = [left,right]
			
	return res
	
arr=[1,2,3,8,9,12,16]
target=122

print(two_sum(arr,target))