# 需求：
# 1. 使用requests库调用TPshop登录功能的相关接口，完成登录操作
# 2. 登录成功后获取‘我的订单’页面的数据
# 3. 要求：使用Session对象来实现
#
import requests
# 获取验证码
session = requests.Session()
response = session.get("http://localhost/index.php?m=Home&c=User&a=verify")
print('第一次cookies:',response.cookies)
# 登录
login_data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
response = session.post("http://localhost/index.php?m=Home&c=User&a=do_login", data=login_data)
print('第二次cookies:',response.cookies)
# print("login response data=", response.json())
# 我的订单
response = session.get("http://localhost/Home/Order/order_list.html")
# print(response.text)
session.close()
