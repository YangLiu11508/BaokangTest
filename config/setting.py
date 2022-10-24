import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)



# 测试环境域名
BASE_URL = 'http://192.168.10.164:8080'

# 执行测试用例套件
#TEST_DIR = './HomePage'
TEST_DIR = './'

# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR,"reports")