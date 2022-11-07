import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/findKnowledgeInfoList?'


class FindKnowledgeInfoList(unittest.TestCase):

    def setUp(self) -> None:
        print('FindKnowledgeInfoList 开始执行...')

    def tearDown(self) -> None:
        print('FindKnowledgeInfoList 结束执行...')

    def test01_findKnowledgeInfoList(self):
        '''
        农技知识页，获取知识大全列表（所有分类）
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test02_science(self):
        '''
        农技知识页，获取科普类列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '040101'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test03_thesis(self):
        '''
        农技知识页，获取论文列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '040102'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test04_patent(self):
        '''
        农技知识页，获取专利列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '040104'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test05_standard(self):
        '''
        农技知识页，获取标准列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '040105'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test06_achievement(self):
        '''
        农技知识页，获取成果列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '040106'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test07_experience(self):
        '''
        农技知识页，获取经验列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '040107'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)
