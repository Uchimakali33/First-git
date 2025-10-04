def min_max(arr,low,high):
	if low==high:
		return arr[low],arr[high]
	if high==low+1:
		if arr[low]<arr[high]:
			return arr[low],arr[high]
		else:
			return arr[high],arr[low]
	mid=(low+high)//2
	
	min1,max1=min_max(arr,low,mid)
	min2,max2=min_max(arr,mid+1,high)
	
	final_min=min(min1,min2)
	final_max=max(max1,max2)
	return final_min,final_max
	
	
minimum=min_max([7,3,9,1,6,4],0,5)

print(minimum)