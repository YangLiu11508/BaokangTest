import unittest
import requests
import json
from config import setting

url = setting.BASE_URL + '/member/county/findNewsType'


class FindNewsType(unittest.TestCase):

    def setUp(self) -> None:
        print('FindNewsType开始执行...')

    def tearDown(self) -> None:
        print('FindNewsType结束执行...')

    def test01(self):

        response = requests.request("GET", url,).json()

        code = response.get('code')
        self.assertEqual(200, code)


