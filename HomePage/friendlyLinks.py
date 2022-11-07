# 友情链接
import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/friendlyLinks'


class FriendlyLinks(unittest.TestCase):

    def setUp(self) -> None:
        print('friendlyLinks开始执行...')

    def tearDown(self) -> None:
        print('friendlyLinks结束执行...')

    def test01_friendlyLinks(self):
        '''
        获取友情链接
        :return:
        '''
        response = requests.request("GET", url).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)
