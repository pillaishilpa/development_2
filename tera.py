import re
import teradata
udaExec = teradata.UdaExec()
session=udaExec.connect(method='odbc',system="blue2040.labs.teradata.com",username="dbc",password="dbc")
for row in session.execute("sel * from dbc.dbcinfo"):
	print row