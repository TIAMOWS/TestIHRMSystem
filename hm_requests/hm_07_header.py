import requests
# 设置请求头
header={"Content-Type":'application/json'}
response=requests.post(url=' http://182.92.81.159/api/sys/login ',json= {"mobile":"13800000002", "password":"123456"},headers=header )
print(response.json())