import re

text = 'gfgfdAAA1234ZZZuijjk'

m = re.search('AAA(.*)', text)
# if m:
#     found = m.group(1)

m =m.group(1)
print(m)