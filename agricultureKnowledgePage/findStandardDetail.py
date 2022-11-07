import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member-reversion/newInformationDetail/findStandardDetail'


class FindStandardDetail(unittest.TestCase):

    def setUp(self) -> None:
        print('findStandardDetail 开始执行...')

    def tearDown(self) -> None:
        print('findStandardDetail 结束执行...')

    def test01_findStandardDetail(self):
        '''
        获取标准规范详情
        :return:
        '''
        payload = "{\"rowNo\":1,\"portalFiled\":\"\",\"docType\":\"\",\"title\":\"\"}"
        headers = {
            'Content-Type': 'text/plain'
        }
        response = requests.request("POST", url, headers=headers, data=payload).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)
