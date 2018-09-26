import re
import os
import sys
from jira import JIRA
c=0
fo=open('a.txt',"w+")
jira = JIRA(server = 'https://jira.td.teradata.com/jira/',basic_auth=('sp186090','mssrrPP15@'))
issue = jira.issue('TDEMAINT-1003')
print issue.fields.assignee
print  issue.fields.status
test_suite= issue.fields.customfield_10510
data=test_suite.encode('ascii','ignore')
print data,type(data)
comment= issue.fields.comment.comments
print comment.body
for i in comment:
	print i.body
