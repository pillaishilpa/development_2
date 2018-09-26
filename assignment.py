import re
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#function to input the value in the corresponding feilds in the web page
def test_case(id,cases,driver):
	case_result=[]
	# get the search textbox
	search_field = driver.find_element_by_id(id)
	# enter search keyword and submit
	for val in cases:
		search_field.clear()
		for j in val:
			k=j+" "
			search_field.send_keys(k)	
		case_result.append(search_field.get_attribute('value'))
	return case_result
	#check_case(id,case_result,cases)

# function to compare the expected result with the web page result
def check_case(id,outlist,expected_list,in_case,fo):
	if id=="phone":
		fo.write('\n------- '+id+' case output '+' -----\n\n') 
		for i in range(len(outlist)):
			if outlist[i]==expected_list[i]:
				fo.write('case_passed '+'input='+" "*25+in_case[i]+" "*25+'output='+" "*25+outlist[i]+"\n\n")
			else:
				fo.write('case_failed '+'input='+" "*25+in_case[i]+" "*25+'output='+" "*25+outlist[i]+"\n\n")
	elif id=='zeroCents':
		fo.write('\n------- '+id+' case output '+' -----\n\n') 
		for i in range(len(outlist)):
			if outlist[i]==expected_list[i]:
				fo.write('case_passed '+'input='+" "*25+in_case[i]+" "*25+'output='+" "*25+outlist[i]+"\n\n") 
			else:
				fo.write('case_failed '+'input='+" "*25+in_case[i]+" "*25+'output='+" "*25+outlist[i]+"\n\n")
	elif id=="numbers":
		fo.write('\n-------  only'+id+' case output '+' -----\n\n')
		for i in range(len(outlist)):
			if outlist[i]==expected_list[i]:
				fo.write('case_passed '+'input='+" "*25+in_case[i]+" "*25+'output='+" "*25+outlist[i]+"\n\n")
			else:
				fo.write('case_failed '+'input='+" "*25+in_case[i]+" "*25+'output='+" "*25+outlist[i]+"\n\n")
				
# function to automatically generate expected results for the input test case
def expected_result(id,inputlist):
	processed_input=[]
	expected_output=[]
	n=0
	k=0
	for val in inputlist:
		temp=""
		for char in val:
			if char>='0' and char<='9' or (id=='numbers' and val[0]=='-'):
				temp=temp+char
		processed_input.append(temp)
	if id=='zeroCents':                       # generating expected result for Zero Cent feild
		for val in processed_input:
			i=0
			val_list=list(val)
			n=(len(val)-1)/3
			k=len(val)%3
			if k>0 and len(val)>3:
				val_list.insert(k,'.')
				n=n-1
			while(i<n):
				if k>0:
					val_list.insert(k+4,'.')
					k=k+4
					i+=1
				elif k<=0:
					val_list.insert(k+3,'.')
					k=k+3
					i+=1
			expected_output.append("".join(val_list)+",00")
			if k<0 and n<1:
				expected_output.append(val)
		return expected_output
	if id=='numbers':                         #  generating expected result for only number feild
		for val in processed_input:
			expected_output.append(val)
		return expected_output
	if id=='phone':                          #  generating expected result for phone number feild
		i=0
		val_list1=[]
		for val in processed_input:
			val_list=list(val)
			if len(val)>2:
				val_list.insert(2,')')
				val_list.insert(3," ")
				if len(val)>6:
					val_list.insert(8,'-')
			n=len(val_list)-13
			if n>0:
				del val_list[-n:]
			if len(val_list)>=1:
				val_list.insert(0,'(')	
			expected_output.append("".join(val_list))
		return expected_output
#main function						
def main():
	phone_list=[]
	zero_cent_list=[]
	only_number_list=[]
	count=0
	fo=open('test_case.txt',"r+")
	list=fo.readlines()
	fo.close()
	fo=open('output.txt',"w+")
	if (re.search(r"phone number",list[count],re.I)):
		count+=1
		while(count):
			if not ((re.search(r"zero cent",list[count],re.I)) or (re.search(r"only number",list[count],re.I))):
				phone_list.append(list[count])
				count+=1
			else:
				break
	if (re.search(r"zero cent",list[count],re.I)):
		count+=1
		while(count):
			if not ((re.search(r"only number",list[count],re.I)) or (re.search(r"phone number",list[count],re.I))):
				zero_cent_list.append(list[count])
				count+=1
			else:
				break
	if (re.search(r"only number",list[count],re.I)):
		count+=1
		while(count<len(list)):
			only_number_list.append(list[count])
			count+=1
	phonelist=[i.strip() for i in phone_list]
	zerocentlist=[i.strip() for i in zero_cent_list]
	onlynumberlist=[i.strip() for i in only_number_list]
	driver = webdriver.Firefox()                                              #create a new Firefox session
	driver.implicitly_wait(30)
	driver.maximize_window()  
	driver.get("https://vanilla-masker.github.io/vanilla-masker/demo.html")   # navigate to the application home page
	expected_list=expected_result('zeroCents',zerocentlist)
	outlist=test_case('zeroCents',zerocentlist,driver)
	check_case('zeroCents',outlist,expected_list,zerocentlist,fo)
	expected_list=expected_result('numbers',onlynumberlist)
	outlist=test_case('numbers',onlynumberlist,driver)
	check_case('numbers',outlist,expected_list,onlynumberlist,fo)
	expected_list=expected_result('phone',phonelist)
	outlist=test_case('phone',phonelist,driver)
	check_case('phone',outlist,expected_list,phonelist,fo)
	fo.close()
	driver.quit()
	
main()





















