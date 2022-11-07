#新闻资讯-通过id查找视频详情

import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/findVideoById?'


class FindVideoById(unittest.TestCase):

    def setUp(self) -> None:
        print('FindVideoById 开始执行...')

    def tearDown(self) -> None:
        print('FindVideoById 结束执行...')

    def test01_find_video_by_id(self):
        '''
        通过id查找视频详情
        :return:
        '''
        params = {'id': 21,
                  'status': 1}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)