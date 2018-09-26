#script to create jiras automatically

import re
from jira import JIRA
fo=open('a.txt',"w+")
jira = JIRA(server = 'https://jira.td.teradata.com/jira/',basic_auth=('sp186090','mssrrPP15@'))
projects=jira.projects()
#print type(projects)
#issue = jira.issue('TDEMAINT-1056')
#jira.add_comment(issue, 'updated DR 188796 with the same.')
issue_dict={'project': 'TDEMAINT',
			'summary': 'observed Failure 3523 in tbf_c2ntsu of Table Functions test',
			'description': 'while testing 16.10.02i.28 build observded Failure 3523 in tbf_c2ntsu of Table Functions test ',
			'issuetype': {'name': 'Bug'},
			    "priority": {"id": "4"}, 'components':[{"name":'bluesky'}]
			}
new_issue = jira.create_issue(fields=issue_dict)
issue = jira.issue('TDEMAINT-1092')
issue.update(assignee={'name': 'sp186090'}) 

	
    