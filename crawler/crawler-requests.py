import requests
# r=requests.get("http://www.baidu.com")
# print(r.status_code)
# r.encoding='utf-8'
# print(r.text)

# print(type(r))
# print(r.headers)


# print(r.text)
# print(r.encoding)
# print(r.apparent_encoding)

# requests post()  自動生成form 
# payload={'key1': 'value1','key2':'value2'}
# r=requests.post('http://httpbin.org/post',data=payload)
# print(r.text)

# requests post()  自動生成data 
# r=requests.post('http://httpbin.org/post',data='ABC')
# print(r.text)

# requests put()  自動生成form 
# payload={'key1': 'value1','key2':'value2'}
# r=requests.put('http://httpbin.org/post',data=payload)
# print(r.text)

#requests.request **kwargs params字典、字節序列，為參數增加到URL中
# kv={'key1': 'value1','key2':'value2'}
# r=requests.request('GET','http://python123.io/ws',params=kv)
# print(r.url)


#requests.request **kwargs data字典、字節序列或文件，作為request的內容
kv={'key1': 'value1','key2':'value2'}
r=requests.request('POST','http://python123.io/ws',data=kv)
body='body content'
r=requests.request('POST','http://python123.io/ws',data=body)
print(r.url)


#requests.request **kwargs json 格式數據，作為request的內容
# kv={'key1': 'value1'}
# r=requests.request('POST','http://python123.io/ws',json=kv)

#requests.request **kwargs header 字典，http
hd={'user-agent':'chrome/10'}
r=requests.request('POST','http://python123.io/ws',headers=hd)
print(r.headers)

#requests.request **kwargs cookie 字典，

#requests.request **kwargs files 字典,傳輸文件
fs={'file':open('data.xls',;rb)}
r=requests.request('POST','http://python123.io/ws',files=fs)
