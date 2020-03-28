# 导包
import requests
# 发送get请求访问百度,传递url的参数有3种方式,
# 第一种:通过url自带的参数来传递
response=requests.get('http://www.baidu.com/S?wd=钟南山')
# # 第二种:通过params参数设置字符串形式的url参数
# response1=requests.get('http://www.baidu.com',params="wd=毒王")
# # 第三种:通过params参数设置字典形式的url参数
# response2=requests.get('http://www.baidu.com',params={"wd":"马云"})


# 打印响应结果
print(response)
print('文本格式的响应体为:',response.text)
