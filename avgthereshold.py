def avg_threshold(arr,k,t):
	i=0
	count=0
	windowsum=0
	for i in range(k):
		windowsum+=arr[i]
		
	if windowsum/k>=t:
		count+=1
		
	for i in range(k,len(arr)):
		windowsum+=arr[i]-arr[i-k]
		
		if windowsum/k>=t:
			count+=1
	return count
	
arr=[2,1,3,4,5]
k=2
t=3

print(avg_threshold(arr,k,t))
		
	