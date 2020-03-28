# 导包
import requests
# 发送post请求,并接受响应数据:对tpshop发送登录请求
response=requests.post(' http://182.92.81.159/api/sys/login ',
                      json={"username":"13800000002"," password":"123456"})
# 打印响应数据
print('响应结果为:',response.text)
# 使用json格式打印数据
print('json格式响应体:',response.json())
