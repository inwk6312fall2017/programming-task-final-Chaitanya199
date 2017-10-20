file = open("running-config.txt","r")
import string

for line in file:
	num =line.replace ('172', '192')
	print (num)

