import requests
import unittest


class Yzm(unittest.TestCase):

    def __init__(self):
        self.session = requests.Session()
        # 发送验证码接口请求
        verify = self.session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        # 获取验证码响应头返回数据
        response_header = verify.headers
        print(f'验证码接口响应头数据:{response_header}')
        # 断言响应头Content-Type值与预期是否一致
        self.assertIn("image", response_header.get("Content-Type"))


