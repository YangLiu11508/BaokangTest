import unittest
import requests
from config import setting

url = setting.BASE_URL + '/member/member/find/1'


class FindStandardDetail(unittest.TestCase):

    def setUp(self) -> None:
        print('findStandardDetail 开始执行...')

    def tearDown(self) -> None:
        print('findStandardDetail 结束执行...')

    def test01_findStandardDetail(self):
        '''
        获取专家团队列表
        :return:
        '''
        payload = "{\"memberType\":\"f413d522b310458aa0bf763012913a0e\",\"status\":1,\"expertType\":\"\",\"memberName\":\"\",\"pageSize\":20,\"pageNum\":1}"
        headers = {
            'Content-Type': 'text/plain'
        }
        response = requests.request("POST", url, headers=headers, data=payload).json()
        code = response.get('code')
        print('response=' + str(response))
        self.assertEqual(200, code)
