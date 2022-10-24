import unittest
import requests
import json
from config import setting

url = setting.BASE_URL + '/member-reversion/videoInfo/getVideo'


class GetVideo(unittest.TestCase):

    def setUp(self) -> None:
        print('GetVideo开始执行...')

    def tearDown(self) -> None:
        print('GetVideo结束执行...')

    def test01(self):

        response = requests.request("GET", url).json()
        code = response.get('code')
        self.assertEqual(200, code)


