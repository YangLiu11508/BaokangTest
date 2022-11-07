# 通过id查找新闻详情
import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/findNewsInformationById?'


class FindNewsInformationById(unittest.TestCase):

    def setUp(self) -> None:
        print('FindNewsInformationById 开始执行...')

    def tearDown(self) -> None:
        print('FindNewsInformationById 结束执行...')

    def test01_find_news_by_id(self):
        '''
        通过id查找新闻详情
        :return:
        '''
        params = {'id': 28,
                  'type': 1,
                  'status': 1}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)