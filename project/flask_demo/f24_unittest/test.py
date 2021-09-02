# encoding:utf8
'''
单元测试  简单案例
'''
import unittest
from login import app
import json

class LoginTest(unittest.TestCase):
    def setUp(self):
        '''在进行测试之前，先被执行，相当于初始化'''

        # 设flask工作在测试模式下
        app.config['TESTING']=True
        # app.testing=True
        # 创建进行web请求的客户端，使用flask提供的
        self.client = app.test_client()

    # 构造单元测试案例(函数必须以test开头，否则不执行测试)
    def test_empty_username_password(self):
        '''测试用户名密码不完整的情况'''

        # 测试用户名和密码都不传

        # 利用client客户端模拟发送web请求
        ret=self.client.post('/login',data={})
        # ret是视图返回的响应对象，data属性是响应体的数据
        resp=ret.data
        # print(resp)
        # 因为login视图返回的是json字符串
        resp=json.loads(resp)
        # 拿到返回值后进行断言测试
        self.assertIn('code',resp)
        self.assertEqual(resp['code'],1)

        # 测试只传用户名

        # 利用client客户端模拟发送web请求
        ret = self.client.post('/login', data={'username':'admin'})
        # ret是视图返回的响应对象，data属性是响应体的数据
        resp = ret.data
        # print(resp)
        # 因为login视图返回的是json字符串
        resp = json.loads(resp)
        # 拿到返回值后进行断言测试
        self.assertIn('code', resp)
        self.assertEqual(resp['code'], 1)

        # 测试只传密码

        # 利用client客户端模拟发送web请求
        ret = self.client.post('/login', data={'password': 'admin'})
        # ret是视图返回的响应对象，data属性是响应体的数据
        resp = ret.data
        # print(resp)
        # 因为login视图返回的是json字符串
        resp = json.loads(resp)
        # 拿到返回值后进行断言测试
        self.assertIn('code', resp)
        self.assertEqual(resp['code'], 1)

    def test_wrong_username_password(self):
        '''测试用户名密码错误的情况'''
        ret=self.client.post('/login',data={'username':'h','password':2})
        resp=ret.data
        resp=json.loads(resp)
        self.assertIn('code', resp)
        self.assertEqual(resp['code'], 2)

if __name__ == '__main__':
    unittest.main()
