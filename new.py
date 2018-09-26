import re
import os
import paramiko
#key = input("Public key full path:")
storage_folder=os.path.abspath('c:\Python27\new6.txt')
try:
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("153.64.26.122",username="root",password="Beagl342")
	print "connection established\n"
	stdin, stdout, stderr = ssh.exec_command("pcl -s pdestate -a")
	print(stdout.read())
	stdin, stdout, stderr = ssh.exec_command("cd pkgs")
	print(stdout.read())
	#stdin.write() can be used to provide the input to the command
	#for transferring file from local to remote or remote to local
	try:
		sftp=ssh.open_sftp()
		sftp.get('/mhmpkg/tdbms-16.10i.00.MHMRSP3-1.x86_64.rpm',storage_folder)
	except Exception as e:
		print str(e)+"error"
except Exception as e:
	print str(e)+" error in ssh connection"