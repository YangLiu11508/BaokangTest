import unittest
import requests
import json
from config import setting

url = setting.BASE_URL + '/member/county/findNewsInformationList?'


class FindNewsInformationList(unittest.TestCase):

    def setUp(self) -> None:
        print('FindNewsInformationList开始执行...')

    def tearDown(self) -> None:
        print('FindNewsInformationList结束执行...')

    def test01(self):
        params = {'pageSize': 5,
                  'pageNum': 1,
                  'type': 2}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        self.assertEqual(200, code)
