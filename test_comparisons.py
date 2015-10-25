import subprocess
import Malwaree1
import sys
import db_connector
FILE = "Malwaree.py"

f = open(FILE, "r")
o = str(Malwaree1.shellcode).encode("hex")
lines = db_connector.selectAll()
print "searching..."
for line in lines:
    if line[1]!="" and line[1] in o:
        print "MALWARE DETECTED"
        print line[1]
        break
    else:
        print "...."
print o
f.close()