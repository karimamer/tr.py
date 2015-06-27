#!/usr/bin/env python2
import subprocess
import sys

f = open(sys.argv[1])
trcomand ="tr -sc 'A-Za-z' '\n' < oscar.txt | sort | uniq -c | sort -n -r | tr -sc 'A-Za-z' | sort -n -r "
runcd = subprocess.check_output(trcomand, shell = True)
try:
	for line in runcd.split('\n'):
		count = line.split(" ")[1]
		word = line.split(" ")[2]
		x =(count,word)
		print x 
       
         

except:
	print "empty line" 	







