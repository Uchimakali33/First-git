def prefix_sum(arr):
	prefixSum=[0]*(len(arr))
	prefixSum[0]=arr[0]
	for i in range(1,len(arr)):
		prefixSum[i]=prefixSum[i-1]+arr[i]
	print(arr)	
	return prefixSum

def diff_arr(arr):
	diffArr=[0]*len(arr)
	diffArr[0]=arr[0]
	
	for i in range(1,len(arr)):
		diffArr[i]=arr[i]-arr[i-1]
	
	return diffArr
		
def query(arr,queries):
	diffAr=diff_arr(arr)
	for left,right,x in queries:
		diffAr[left]+=x
		diffAr[right+1]-=x
		
	return prefix_sum(diffAr)
	
arr = [2, 3, 1, 4, 0, 5, 2]
queries = [
    [1, 3, 5],   # Add 5 to arr[1..3]
    [2, 5, 2],   # Add 2 to arr[2..5]
    [0, 4, 1]    # Add 1 to arr[0..4]
]

print(query(arr,queries))
		
	