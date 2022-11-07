# 首页种植场数量
import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/farmCount'


class FarmCount(unittest.TestCase):

    def setUp(self) -> None:
        print('farmCount开始执行...')

    def tearDown(self) -> None:
        print('farmCount结束执行...')

    def test01_farmCount(self):
        response = requests.request("GET", url).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)
