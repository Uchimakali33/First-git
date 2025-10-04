def anagram(s,t):
	if len(s) != len(t):
		return False
	hashs={}
	hasht={}
	
	for i in range(len(s)):
		elementS=s[i]
		if elementS in hashs:
			hashs[elementS]+=1
		else:
			hashs[elementS]=1
		elementT=t[i]
			
		if elementT in hasht:
			hasht[elementT]+=1
		else:
			hasht[elementT]=1
			
	if hashs==hasht:
		return True
	else:
		return False
		
print(anagram('eat','te'))