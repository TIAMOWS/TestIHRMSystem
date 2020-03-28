import requests

session=requests.Session()
# 登录接口
header={"Content-Type":"application/json"}
data={"mobile":"13800000002","password":"123456"}
respons=session.post('http://182.92.81.159/api/sys/login',json=data,headers=header)
print(respons.json())

print('*'*20)

respons1=session.post('http://182.92.81.159/api/sys/profile')

print(f'url:{respons1.url}')
print(f'encoding:{respons1.encoding}')
print(f'cookies:{respons1.cookies}')
print(f'headres:{respons1.headers}')

print('*'*20)

print(respons1.json())
