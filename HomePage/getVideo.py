# 首页视频
import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member-reversion/videoInfo/getVideo'


class GetVideo(unittest.TestCase):

    def setUp(self) -> None:
        print('GetVideo开始执行...')

    def tearDown(self) -> None:
        print('GetVideo结束执行...')

    def test01_getVideo(self):
        '''
        首页获取视频
        :return:
        '''
        response = requests.request("GET", url).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)
