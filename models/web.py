import urllib.request
import urllib.parse
import ssl
"""
ssl._create_default_https_context = ssl._create_unverified_context
url = "http://pythonprogramming.net"
values= {'q':'basic'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)
"""
# x = urllib.request.urlopen('http://www.baidu.com')
# print(x.read().decode())

try:
    ssl._create_default_https_context = ssl._create_unverified_context
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))



try:
    url = 'https://www.google.com/search'
    headers = {}
    headers['user_agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    # print(resp.read())

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(resp.read()))
    saveFile.close()
except Exception as e:
    print(str(e))