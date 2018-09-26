#om sai ram
import re
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
phone_expected_result=['(1','(12','(12) 3','(12) 34','(12) 3','(12) 3456-78','(12) 3456','(12) 3456-7890','(91) 1234-5678','','(91) 1234-5678']
zero_cent_expected_result=['123,00','0,00','12,00','1.234,00','1.234.567.890,00','345.677,00','1.233.678,00']
number_only_expected_result=['1233','-1234','12343','','12345','12323455']

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
	check_case(id,case_result,cases)
	
def check_case(id,list,in_case):
	if id=="phone":
		print '-------',id,'case output','-----\n'
		for i in range(len(list)):
			if list[i]==phone_expected_result[i]:
				print 'case_passed','input=',in_case[i],'output=',list[i],"\n"
			else:
				print 'case_failed','input=',in_case[i],'output=',list[i],"\n"
	elif id=='zeroCents':
		print '-------',id,'case output','-----\n'
		for i in range(len(list)):
			if list[i]==zero_cent_expected_result[i]:
				print 'case_passed','input=',in_case[i],'output=',list[i],"\n"
			else:
				print 'case_failed','input=',in_case[i],'output=',list[i],"\n"
	elif id=="numbers":
		print '-------',id,'case output','-----\n'
		for i in range(len(list)):
			if list[i]==number_only_expected_result[i]:
				print 'case_passed','input=',in_case[i],'output=',list[i],"\n"
			else:
				print 'case_failed','input=',in_case[i],'output=',list[i],"\n"
def main():
	phone_list=[]
	zero_cent_list=[]
	only_number_list=[]
	count=0
	fo=open('test_case.txt',"r+")
	list=fo.readlines()
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
	# create a new Firefox session
	driver = webdriver.Firefox()
	driver.implicitly_wait(30)
	driver.maximize_window()
	# navigate to the application home page
	driver.get("https://vanilla-masker.github.io/vanilla-masker/demo.html")
	test_case('phone',phonelist,driver)
	test_case('numbers',onlynumberlist,driver)
	test_case('zeroCents',zerocentlist,driver)
	driver.quit()
	
main()





















