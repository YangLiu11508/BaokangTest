import unittest
import requests
import json
from config import setting

url = setting.BASE_URL + '/member/memberIntroduce/findMemberIntroduceInfo'


class FindMemberIntroduceInfo(unittest.TestCase):

    def setUp(self) -> None:
        print('FindMemberIntroduceInfo开始执行...')

    def tearDown(self) -> None:
        print('FindMemberIntroduceInfo结束执行...')

    def test01(self):
        payload = "{\"account\":\"bkx111111\"}"
        headers = {
            'Content-Type': 'text/plain'
        }
        response = requests.request("POST", url, headers=headers, data=payload).json()
        code = response.get('code')
        self.assertEqual(200, code)


