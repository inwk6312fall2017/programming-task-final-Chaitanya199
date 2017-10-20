file = open ("running-config.txt", "r")
import string

line = file.read()
word = line.strip(' ')
mm = word.split()

access_list_name = []
access_list = []

for i in range (len(mm)):
        if mm[i] == 'access_list':
                access_list_name.append(mm[i+1])

for i in range (len(access_list_name)):
	print ("access_list[i]", "-->") 
