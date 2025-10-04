def merge_sort(arr):
	
	if len(arr)<=1:
		return arr
		
	mid=len(arr)//2
	
	left_half=merge_sort(arr[:mid])
	right_half=merge_sort(arr[mid:])
	
	return merge(left_half,right_half)
	
def merge(left,right):
	
	i=0
	j=0
	result=[]
	
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
			
	result.extend(left[i:])
	result.extend(right[j:])
	
	return result
	
arr=[37,4,23,2,8,20,89,23]

print(f'original arr {arr}')
print(f'sorted arr {merge_sort(arr)}')