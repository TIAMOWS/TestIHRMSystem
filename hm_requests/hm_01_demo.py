# 导包
import requests
# 发送get请求访问百度
response=requests.get('http://www.baidu.com')
# 打印响应结果
print(response)
print('文本格式的响应体为:',response.text)

