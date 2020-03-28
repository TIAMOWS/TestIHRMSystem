# 导包
import requests
# 发送get请求访问百度
response=requests.get('http://www.weather.com.cn/data/sk/101010100.html')

# 打印响应结果
print(response)
print('json格式的响应体为:',response.json())
# 字节码解析
response.content.decode(encoding='utf-8')
response.encoding='utf-8'
print('转码后json格式的响应体为:',response.json())
