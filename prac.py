import re
"""str1='shilpa'
str2='abcshhilpaaxyz'
flg=0
for ch in str1:
	if str2.count(ch)>=str1.count(ch):
		pass
	else:
		flg=1
		break
if flg==1:
	print 'not ok'
else:
	print 'ok'"""
# reveres string
#method 1
str=" i am a good girl"
print str[::-1]
#method 2
str_lst=[]
i=len(str)-1
while(i>=0):
	str_lst.append(str[i])
	i-=1
str2=''.join(str_lst)
print str2
#method 3
s=""
for ch in str:
	s=ch+s
print s
lst=str.split()
print lst
print ' '.join(reversed(lst)) # reversed(lst) gives the object pointing to last index of the input list
print ' '.join(lst[::-1])
s=int(raw_input('enter a number:'))
k=int(raw_input('enter the value of k:'))
count=0
tem=s
while(temp>0):
	count+=1
	temp=temp/10
print count


	