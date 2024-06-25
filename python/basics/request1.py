"""
DOC: https://docs.python.org/3/library/urllib.html
     https://docs.python.org/3/library/urllib.request.html#module-urllib.request
     https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse


"""

import urllib.request, urllib.parse
import json

"""
GET
urllib.request.urlopen for get request
urllib.parse.urlencode for params
"""

payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# print(url)

# with urllib.request.urlopen(url) as f:
#     print(json.loads(f.read().decode('utf-8')))

"""
POST
urllib.request.Request
"""
payload = json.dumps(payload).encode('utf-8') # post, put, deleteのpayloadはenodeする必要がある

req = urllib.request.Request('http://httpbin.org/post', data=payload, method='POST')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

"""
PUT
urllib.request.Request
"""
req = urllib.request.Request('http://httpbin.org/put', data=payload, method='PUT')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

"""
DELETE
urllib.request.Request
"""
req = urllib.request.Request('http://httpbin.org/delete', data=payload, method='DELETE')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))