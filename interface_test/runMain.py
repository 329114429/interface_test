# 导入包 unittest , HTMLTestRunner

# 第一步 组装测试套件， 第二步， 置顶存放报告的路径， 第三步，运行测试套件并生成测试报告

import unittest
import time
from HTMLTestRunner import HTMLTestRunner

# 第一步是组装测试套件
suite = unittest.defaultTestLoader.discover("./testcases", pattern="test*.py")

# 第二步存放测试报告路径及名称
file_path = "./reports/{}.html".format(time.strftime("%Y-%m-%d %H:%M:%S"))

# 运行测试套件并生成测试报告
with open(file_path, "w") as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="测试报告", description=u"用例执行情况")
    runner.run(suite)
    f.close()
