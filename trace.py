import sys
import os
import re
import spur
shell = spur.SshShell(hostname="blue4501.labs.teradata.com", username="root", password="Beagl342")
result = shell.run("ls")
print result.output