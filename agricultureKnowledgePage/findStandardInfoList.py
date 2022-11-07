import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/findStandardInfoList?'


class FindStandardInfoList(unittest.TestCase):

    def setUp(self) -> None:
        print('findStandardInfoList 开始执行...')

    def tearDown(self) -> None:
        print('findStandardInfoList 结束执行...')

    def test01_findStandardInfoList(self):
        '''
        标准规范列表
        :return:
        '''
        params = {'pageSize': 10,
                  'pageNum': 1}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test02_findStandardInfoList(self):
        '''
        标准规范搜索功能
        :return:
        '''
        params = {'pageSize': 10,
                  'pageNum': 1,
                  'title': '猪'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)
