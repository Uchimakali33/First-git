hash=[0]*26
que=[]
def pre_compute(string):
	for i in string:
		hash[ord(i)-ord('a')]+=1
		
def queries(que):
	for i in que:
		print(hash[ord(i)-ord('a')])
	
		
def data_input():
	string=input()
	q=int(input())
	for i in range(q):
		qu=input()
		que.append(qu)
	pre_compute(string)
	queries(que)
data_input()
print(hash)
print(que)