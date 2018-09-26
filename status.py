import os
import sys
import getpass
import re
from jira import JIRA
import xlsxwriter
from time import strftime
import teradata
import pyodbc

def Yearly_Report(Build_Jira,Status_Dict):
	temp = 0
	while (temp < len(Build_Jira)):
		#print (Build_Jira[temp].fields.assignee.displayName)
		Status_Dict[Build_Jira[temp].fields.assignee.displayName][0][0] = Status_Dict[Build_Jira[temp].fields.assignee.displayName][0][0] + 1
		Status_Dict[Build_Jira[temp].fields.assignee.displayName][1][0] = Status_Dict[Build_Jira[temp].fields.assignee.displayName][1][0] + (int(Build_Jira[temp].fields.labels[0]))
		temp = temp + 1
	Defect(Status_Dict)

def Defect(Status_Dict):
	udaExec = teradata.UdaExec (appName="HelloWorld", version="1.0",logConsole=False)
	temp = pyodbc.drivers()
	i = 0 
	while (i < len(temp)):
		print temp[i]
		if (temp[i].find("Teradata Database ODBC Driver ") != -1):
			Odbc_drive = temp[i]
			session = udaExec.connect(authentication="LDAP",method="odbc", system="biggulp", username=jira_user, password=jira_password, driver=Odbc_drive)
			break;
		i = i + 1
	i = 0
	while (i < len(QuickLook)):
		query = "sel count(distinct Change_Number) from  DARTS.pc_base where Author_Person_ID='" + QuickLook[i] + "' and Created_Datetime  between '2018-01-01 00:00:00' and current_timestamp(6);"
		for row in session.execute(query):
			data =re.findall(r"\[\w+\]",str(row))
			DR_Count = int(data[0][1:-1])
		Status_Dict[User[i]][2][0] = Status_Dict[User[i]][2][0] + DR_Count
		i = i + 1
	
def Doc_Ment(User, Status_Dict):
	Doc_List =[["Name","Actual # of Test cases-DRs","Actual # of Scenarios" ,"Total # of DRs Open"]]
	i = 0
	Total_Jira = 0
	Total_Scenarios = 0
	Total_DR = 0
	while (i < len(User)):
		Total_Jira = Total_Jira + Status_Dict[User[i]][0][0]
		Total_Scenarios = Total_Scenarios + Status_Dict[User[i]][1][0]
		Total_DR = Total_DR + Status_Dict[User[i]][2][0]
		Doc_List = Doc_List + [[User[i], Status_Dict[User[i]][0][0], Status_Dict[User[i]][1][0], Status_Dict[User[i]][2][0]]]
		i = i + 1	
	Doc_List = Doc_List + [["Total", Total_Jira, Total_Scenarios, Total_DR]]
	#print(Doc_List)
	ws = wb.add_worksheet("Yearly")
	
	ws.set_column(0,3,30)
	for row in range(0, len(Doc_List)):
		for col in range(0, len(Doc_List[0])):
			ws.write(row, col, Doc_List[row][col])
	
	wb.close()
def main():
	Build_Jira = jira.search_issues('project = TDETE AND assignee in (sk185133,sk186001,nr250008,ma186014, as186177, jr186011, rp255005, sl255016, sb186061) and status = Closed and updated >= startOfYear()  and text ~ "Interact DR* Scenario with other SQL Features." and type = story and component="DR Test Dev"  ORDER BY priority DESC, updated DESC')
	i=0
	Status_Dict = {}
	while (i < len(User)):
		Status_Dict.update({User[i]: [[0],[0],[0]]})
		#status_dict = {"Korukonda, Srinivasa" : [[],[]],"Rajanala, Nagamary" : [[],[]], "Shaik, Mansoor" : [[],[]], "Shareef Moghal, Ali": [[],[]], "Reddy, Jeevan B": [[],[]], "Padala, Raju": p[[],[]], "Lysetti, Sateesh": [[],[]],"Bsk, Shahul Hameed":[[],[]]}
		i = i + 1
	
	Yearly_Report(Build_Jira,Status_Dict)
	Doc_Ment(User,Status_Dict)
	input("Enter to Exit : ")
	
	


jira_user = input("Enter your QuickLook ID : ")
jira_password = getpass.getpass("Enter your Password : ")
try:
	jira = JIRA(server = 'https://jira.td.teradata.com/jira/',basic_auth=(jira_user,jira_password)) 
except Exception as e:
	print (str(e) + " Error occurred while connecting to JIRA , Check the user name password and other details")
	sys.exit(0);
	
log=strftime(("%d-%m-%Y-%H-%M-%S"))
wb = xlsxwriter.Workbook('TDETE_STATUS-'+log+'.xlsx')
User = ["Korukonda, Srinivasa","Rajanala, Nagamary","Korepella, Sriram", "Shaik, Mansoor", "Shareef Moghal, Ali", "Reddy, Jeevan B", "Padala, Raju", "Lysetti, Sateesh","B sk, Shahul"]
QuickLook = ["SK185133", "NR250008", "SK186001", "MA186014", "AS186177", "JR186011", "RP255005", "SL255016", "SB186061" ]
main()