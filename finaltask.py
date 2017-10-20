file1 = open ("Book1.txt")
file2 = open ("Book2.txt")
file3 = open ("Book3.txt")

import string

"""for line1 in file1:
	line1 = line1.strip()
	for word1 in line1:
		word1 = line1.split()
	print (word1)

for line2 in file2:
	line2 = line2.strip()
	for word2 in line2:
		word2 = line2.split()
	print (word2)"""

for line in file3:
	word = line.strip()
	word = line.split()
	print (word)


