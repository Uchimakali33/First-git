
def maxsub_arr(arr,k):
	windowsum=0
	for i in range(k):
		windowsum+=arr[i]
	maxsum=windowsum
	
	for i in range(k,len(arr)):
		windowsum+=arr[i]-arr[i-k]
		maxsum=max(windowsum,maxsum)
	return maxsum
	
arr=[1,2,1,3,5,2]
k=3
print(maxsub_arr(arr,k))
			
		
		