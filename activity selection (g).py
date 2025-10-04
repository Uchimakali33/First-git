def activity_selection(arr):
	arr.sort(key=lambda x:x[1])
	
	result=[]
	last_end=-1
	
	for start,end in arr:
		if start>=last_end:
			result.append((start,end))
			last_end=end
			
	return result,len(result)
	
arr=[(1,3), (2,5), (4,6), (6,7), (5,9), (8,9)]

res,count=activity_selection(arr)
print(res)
print(count)
