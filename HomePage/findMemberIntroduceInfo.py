# 黄龙观，中坪村，尧治河村 概况

import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/memberIntroduce/findMemberIntroduceInfo'


class FindMemberIntroduceInfo(unittest.TestCase):

    def setUp(self) -> None:
        print('FindMemberIntroduceInfo开始执行...')

    def tearDown(self) -> None:
        print('FindMemberIntroduceInfo结束执行...')

    def test01_zpc(self):
        '''
        中坪村概况
        :return:
        '''
        payload = "{\"account\":\"zpc111111\"}"
        headers = {
            'Content-Type': 'text/plain'
        }
        response = requests.request("POST", url, headers=headers, data=payload).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test02_hlg(self):
        '''
        黄龙观村概况
        :return:
        '''
        payload = "{\"account\":\"hlg111111\"}"
        headers = {
            'Content-Type': 'text/plain'
        }
        response = requests.request("POST", url, headers=headers, data=payload).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)

    def test03_yzh(self):
        '''
        尧治河村概况
        :return:
        '''
        payload = "{\"account\":\"yzh111111\"}"
        headers = {
            'Content-Type': 'text/plain'
        }
        response = requests.request("POST", url, headers=headers, data=payload).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)
