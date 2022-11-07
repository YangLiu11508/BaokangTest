# 新闻资讯页视频列表

import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/findVideoList?'


class FindVideoList(unittest.TestCase):

    def setUp(self) -> None:
        print('findVideoList 开始执行...')

    def tearDown(self) -> None:
        print('findVideoList 结束执行...')

    def test01_findVideoList(self):
        '''
        新闻资讯-视频列表
        :return:
        '''
        params = {'pageSize': 3,
                  'pageNum': 1,
                  'status': 1}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)
