def prefix_sum(arr):
	prefixSum=[0]*(len(arr))
	prefixSum[0]=arr[0]
	for i in range(1,len(arr)):
		prefixSum[i]=prefixSum[i-1]+arr[i]
	print(arr)	
	print(prefixSum)
	return prefixSum
	

	
def queries(arr,query):
	pre=prefix_sum(arr)
	for left,right in query:
		if left==0:
			print(pre[right])
		else:
			print(pre[right]-pre[left-1])
	return 'success'
		
arr = [2, 4, 1, 3, 5]
query = [(0, 2), (1, 3), (2, 4)]
print(f'with queries {queries(arr,query)}')