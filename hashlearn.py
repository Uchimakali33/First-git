hash=[0]*13

def count_arr(n,arr):
	for i in range(n):
		hash[arr[i]]+=1
		
def query(que):
	print('count of que ',hash[que])
		
n=int(input())
arr=list(map(int,input().split(' ')))
count_arr(n,arr)

q=int(input())
for i in range(q):
	que=int(input())
	query(que)
	

		
	
	
	