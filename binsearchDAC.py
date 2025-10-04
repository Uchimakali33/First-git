def rbin_search(low,high,key,arr):
	if low > high:
		return -1
	
	mid=(low+high)//2
	if arr[mid]==key:
		return mid
	elif arr[mid]>key:
		return rbin_search(low,mid-1,key,arr)
	else:
		return rbin_search(mid+1,high,key,arr)	
arr=[10,20,30,40,50]
result=rbin_search(0,len(arr),5,arr)
print(result)
