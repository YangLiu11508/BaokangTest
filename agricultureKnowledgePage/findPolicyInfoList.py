import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/county/findPolicyInfoList?'


class FindPolicyInfoList(unittest.TestCase):

    def setUp(self) -> None:
        print('findPolicyInfoList 开始执行...')

    def tearDown(self) -> None:
        print('findPolicyInfoList 结束执行...')

    def test01_findPolicyInfoList(self):
        '''
        农技知识页，获取法律法规列表（所有分类）
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test01_laws(self):
        '''
        农技知识页，获取政策法规列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '030201'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test02_understand(self):
        '''
        农技知识页，获取政策解读列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '030202'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)


    def test03_party(self):
        '''
        农技知识页，获取党务动态列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '030209'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test04_government(self):
        '''
        农技知识页，获取政务动态列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '030210'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)


    def test05_rule(self):
        '''
        农技知识页，获取民规民约列表
        :return:
        '''
        params = {'pageSize': 6,
                  'pageNum': 1,
                  'docType': '030211'}
        response = requests.request("GET", url, params=params).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)