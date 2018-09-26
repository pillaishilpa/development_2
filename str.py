import re
new_lst=[]
str=raw_input("enter a string\n")
lst=list(str)
"""for i in lst:
	if i not in new_lst:
		new_lst.append(i)
	else:
		continue
new_string=''.join(new_lst)
print str+"\n"
print new_string+"\n" """
new_lst=[]
new_lst[0]=lst[0]
i=1
while(i<len(lst)-1):
	if lst[i-1]!=lst[i] and lst[i+1]!=lst[i]:
		new_lst.append(lst[i])
new_str=''.join(new_lst)
