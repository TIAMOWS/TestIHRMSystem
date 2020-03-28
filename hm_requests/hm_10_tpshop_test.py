import unittest
import requests


class TpshopLoginTest(unittest.TestCase):
    """测试tpshop商城登录模块"""

    def setUp(self):
        # 实例化session对象
        self.session = requests.Session()
        # 发送验证码接口请求
        verify = self.session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        # 获取验证码响应头返回数据
        response_header = verify.headers
        print(f'验证码接口响应头数据:{response_header}')
        # 断言响应头Content-Type值与预期是否一致
        self.assertIn("image", response_header.get("Content-Type"))

    def tearDown(self):
        self.session.close()


    def test01_login(self):
        """测试登录成功"""
        # 发送登录接口请求
        login_url = self.session.post("http://localhost/index.php?m=Home&c=User&a=do_login",
                                      data={"username": "13800138006",
                                            "password": "123456",
                                            "verify_code": "8888"})
        # 获取返回响应数据
        json_data = login_url.json()
        print(f'登录结果为:{json_data}')

        # 断言响应数据中,响应状态码,status,msg,的值
        self.assertEqual(200, login_url.status_code)  # 断言响应转态码
        self.assertEqual(1, json_data.get("status"))  # 断言返回json数据中status的值
        self.assertEqual("登陆成功", json_data.get("msg"))  # 断言返回json数据中的msg的值

    def test02_username_not_exist(self):
        """测试账号不存在"""
        # 发送登录接口请求
        login_url = self.session.post("http://localhost/index.php?m=Home&c=User&a=do_login",
                                      data={"username": "138001380677",
                                            "password": "123456",
                                            "verify_code": "8888"})
        # 获取返回响应数据
        json_data = login_url.json()
        print(f'登录结果为:{json_data}')

        # 断言响应数据中,响应状态码,status,msg,的值
        self.assertEqual(200, login_url.status_code)  # 断言响应转态码
        self.assertEqual(-1, json_data.get("status"))  # 断言返回json数据中status的值
        self.assertEqual("账号不存在!", json_data.get("msg"))  # 断言返回json数据中的msg的值

    def test03_password_error(self):
        """测试密码错误"""

        # 发送登录接口请求
        login_url = self.session.post("http://localhost/index.php?m=Home&c=User&a=do_login",
                                      data={"username": "13800138006",
                                            "password": "123476",
                                            "verify_code": "8888"})
        # 获取返回响应数据
        json_data = login_url.json()
        print(f'登录结果为:{json_data}')

        # 断言响应数据中,响应状态码,status,msg,的值
        self.assertEqual(200, login_url.status_code)  # 断言响应转态码
        self.assertEqual(-2, json_data.get("status"))  # 断言返回json数据中status的值
        self.assertEqual("密码错误!", json_data.get("msg"))  # 断言返回json数据中的msg的值