name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle :
    lst=line.split()
    if len(lst)==0 or lst[0]!='From' :
        continue
    counts[lst[1]]=counts.get(lst[1], 0) + 1

maxK=None
maxV=None
for k,v in counts.items() :   
    if maxV is None or v > maxV :
        maxV=v
        maxK=k
print(maxK,maxV)