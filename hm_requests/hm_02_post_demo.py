# 导包
import requests
# 发送post请求,并接受响应数据:对tpshop发送登录请求
response=requests.post('http://localhost/index.php?m=Home&c=User&a=do_login',
                       data={"username":"13088888888"," password":"123456","verify_code":"1234"})
# 打印响应数据
print('响应结果为:',response.text)
# 使用json格式打印数据
print('json格式响应体:',response.json())

