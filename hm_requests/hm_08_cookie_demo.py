# 导包
import requests
# 发送获取验证码请求
responses_verify=requests.get(url='http://localhost/index.php?m=Home&c=User&a=verify')
# 获取验证码返回的数据
back_verify=responses_verify.content
print('返回的验证码:',back_verify)
# 获取验证码返回的cookies
cookies=responses_verify.cookies
print(cookies)
# 发送登录请求,从验证码吗中获取的cookies给服务器
respons=requests.post('http://localhost/index.php?m=Home&c=User&a=do_login',
                      data={"username":"13088888888",
                            " password":"123456",
                            "verify_code":"1234"},
                      cookies=cookies )
# 打印登录数据
print('登录数据',respons.json())
# 发送我的订单接口请求
order=requests.get
