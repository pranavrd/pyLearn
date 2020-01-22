import re

fh=open("regex_sum.txt")

sum=0

for line in fh :
	line=line.rstrip()
	x=re.findall('[0-9]+',line)
	if len(x)==0 : continue
	for it in x :
		sum+=int(it)

print(sum)