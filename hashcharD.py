dict={}
queries=[]
def pre_compute(string):
	for i in string:
		if i in dict:
			dict[i]+=1
		else:
			dict[i]=1

def query(que):
	for i in range(que):
		queries.append(input().strip())
	
def fetch(queries):
	for i in queries:
		if i in dict:
			print(dict[i])
		else:
			print(0)	

string=input().strip()
pre_compute(string)
que=int(input())
query(que)
fetch(queries)

