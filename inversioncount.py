def countinversqion(arr):
	if len(arr)<=1:
		return arr,0
	mid=len(arr)//2	
	left,inv_left=countinversion(arr[:mid])
	
	right,inv_right=countinversion(arr[mid:])
	
	merged,inv_split=mergeandcount(left,right)
	
	return merged,inv_left+inv_right+inv_split
	
def mergeandcount(left,right):
	i=j=0
	merged=[]
	inv_count=0
	
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			merged.append(left[i])
			i+=1
		else:
			merged.append(right[j])
			inv_count+=(len(left)-i)
			j+=1
	merged.extend(left[i:])
	merged.extend(right[j:])
		
	return merged,inv_count
	
arr=[2,4,1,3,5]
lst,count=countinversion(arr)
print(count)
			