# 首页 新闻列表列表,保康县概况
import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/findNewsInformationList?'


class FindNewsInformationList(unittest.TestCase):

    def setUp(self) -> None:
        print('FindNewsInformationList开始执行...')

    def tearDown(self) -> None:
        print('FindNewsInformationList结束执行...')

    def test01_agriculture_news(self):
        '''
        农业要闻列表
        :return:
        '''
        params = {'pageSize': 5,
                  'pageNum': 1,
                  'type': 2}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test02_bk_introduction(self):
        '''
        保康县概况
        :return:
        '''
        params = {'type': 5}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test03(self):
        '''
        新闻资讯-通知公告列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'type': 1,
                  'status': 1}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test04(self):
        '''
        新闻资讯-新闻热点，资讯中心列表（所有分类）
        :return:
        '''
        params = {'pageSize': 14,
                  'pageNum': 1,
                  'type': 2,
                  'status': 1}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test05(self):
        '''
        新闻资讯-乡村动态
        :return:
        '''
        params = {'pageSize': 14,
                  'pageNum': 1,
                  'type': 2,
                  'status': 1,
                  'newsType': 1}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test06(self):
        '''
        新闻资讯-农业动态
        :return:
        '''
        params = {'pageSize': 14,
                  'pageNum': 1,
                  'type': 2,
                  'status': 1,
                  'newsType': 2}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test07(self):
        '''
        新闻资讯-政策专题
        :return:
        '''
        params = {'pageSize': 14,
                  'pageNum': 1,
                  'type': 2,
                  'status': 1,
                  'newsType': 3}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test08(self):
        '''
        新闻资讯-通知公告搜索
        :return:
        '''
        params = {'pageSize': 8,
                  'pageNum': 1,
                  'type': 1,
                  'status': 1,
                  'title': '测试'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)