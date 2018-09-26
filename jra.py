from jira import JIRA
import sys
import getpass
user_name=raw_input("enter the  user name : ")
password=getpass.getpass("enter password: ")
try:
	jira = JIRA(server = 'https://jira.td.teradata.com/jira/',basic_auth=(user_name,password))
	#options = {
    #'server': 'https://jira.atlassian.com'}
	#jira = JIRA(options)
	#jira=JIRA(server='https://jira.td.teradata.com/jira/',basic_auth=(user_name,password))
except Exception as e:
	print(str(e))+("error")
	sys.exit(0)
#projects=jira.projects()
#print projects
#issues=jira.search_issues('assignee=Shipa,Pillai')
issues = jira.search_issues('project = TDEEFIX AND component = "E-Fix triage" ',0,10)
print issues
"""from bs4 import BeautifulSoup as bsf
import urllib2
url = 'http://google.com/search?q=word'
req = req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser",'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
response=urllib2.urlopen(req)
html=response.read()
print html"""
