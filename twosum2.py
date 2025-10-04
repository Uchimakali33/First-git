def two_sum2(arr,k):
	left=0
	right=len(arr)-1
	sum=0
	while left<right:
		sum=arr[left]+arr[right]
		if sum>k:
			right-=1
		elif sum<k:
			left+=1
		else:
			return [left+1,right+1]
			
print(two_sum2([0,-1],-1))
			