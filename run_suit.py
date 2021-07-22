import unittest
import time
import app

from htmltestrunner3 import HTMLTestRunner
from script.test01_login import TestLogin
from script.test02_sub import TestSub


# 封装
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestSub))

# 指定报告文件路径
report = app.Base_DIR + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 文件流形式打开文件
with open(report, "wb") as f:
    # 创建HTMLTestRunner
    runner = HTMLTestRunner(f, title="商家端测试报告")

    runner.run(suite)
