
count={}
que=[]
def count_num(arr):
	for i in arr:
		if i in count:
			count[i]+=1
		else:
			count[i]=1
			
def fetch(query):
	for i in query:
		if i in count:
			print(count[i])
		else:
			print(0)

n=int(input())
arr=list(map(int,input().split()))
count_num(arr)
q=int(input())
for i in range(q):
	qu=int(input())
	que.append(qu)
fetch(que)

				
		