# 农技知识页，获取知识大全分类
import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/findEssayType?'


class FindEssayType(unittest.TestCase):

    def setUp(self) -> None:
        print('findEssayType 开始执行...')

    def tearDown(self) -> None:
        print('findEssayType 结束执行...')

    def test01_findEssayType(self):
        '''
        农技知识页，获取知识大全分类
        :return:
        '''
        params = {'tableName': 'Knowledge'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

