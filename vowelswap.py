def vowels_swap(str1,str2):
	i=0
	j=0
	res1=''
	res2=''
	while i<len(str1) and j<len(str2):
		if str1[i] not in 'aeiouAEIOU':
			res1+=str1[i]
		elif str2[j] not in 'AEIOUaeiou':
			res2+=str2[j]
		else:
			res1+=str2[j]
			res2+=str1[i]
			i+=1
			j+=1
	print(res1)
	print(res2)
	
str1='environment'
str2='auditorium'

vowels_swap(str1,str2)
	