import unittest
from config import setting
import os
import time
import HTMLTestRunner

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(findMemberIntroduceInfo.FindMemberIntroduceInfo('test01'))
    # suite.addTest(getVideo.GetVideo('test01'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # 按照路径加载测试用例
    # 过滤装载器：defaultTestLoader.discover
    all_tests = unittest.defaultTestLoader.discover(start_dir=setting.TEST_DIR, pattern='*.py')
    # start_dir筛选路径, pattern筛选文件名
    # 默认装载器，可以执行指定路径，指定名字的测试模块，'./'表示当前文件夹，TestCase*.py表示前缀是Testcase的文件都会被执行
    # 过滤为当前文件夹下以TestCase为前缀的用例，我们用例为TestCases且在当前文件夹，因此会执行
    # runner = unittest.TextTestRunner()

    # 调用HTMLTestRunner生成测试报告
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = os.getcwd() + '/reports/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口自动化测试报告',
                                           description='环境：windows 10 浏览器：chrome',
                                           tester='yangliu')
    runner.run(all_tests)
    fp.close()
