import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tval = 0

address = input('Enter location: ')
url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
info = json.loads(data)

total=0

for k,v in info.items():
	if k=='comments' :
		for val in v :
			for key,value in val.items():
				if key=='count' :
					total=total+value

print(total)
