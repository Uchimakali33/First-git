arr=["eat","tea","tan","ate","nat","bat"]
hash={}

for s in arr:
	s_sorted=sorted(s)
	key=tuple(s_sorted)
		
	if key in hash:
		hash[key].append(s)
	else:
		hash[key]=[s]
		
res=hash.values()
print(list(res))
			
		
		