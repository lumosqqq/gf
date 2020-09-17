import unittest
import test  # 引用一下计算程序，不然代码属实太长
from BeautifulReport import BeautifulReport

class TestForAllText(unittest.TestCase):

    def test_add(self):

        test.simi('orig.txt', 'orig_self5.txt', 'D:/xx.txt')
    def test_del(self):

        test.simi('orig.txt', 'orig_0.8_del.txt', 'D:/xx.txt')

    def test_dis_1(self):

        test.simi('orig.txt', 'orig_0.8_dis_1.txt', 'D:/xx.txt')
    def test_dis_3(self):

        test.simi('orig.txt', 'orig_0.8_dis_3.txt', 'D:/xx.txt')
    def test_dis_7(self):

        test.simi('orig.txt', 'orig_0.8_dis_7.txt', 'D:/xx.txt')
    def test_dis_10(self):

        test.simi('orig.txt', 'orig_0.8_dis_10.txt', 'D:/xx.txt')
    def test_dis_15(self):

        test.simi('orig.txt', 'orig_0.8_dis_15.txt', 'D:/xx.txt')
    def test_mix(self):

        test.simi('orig.txt', 'orig_0.8_mix.txt', 'D:/xx.txt')
    def test_rep(self):
        test.simi('orig.txt', 'orig_0.8_rep.txt', 'D:/xx.txt')
    def test_self(self):
        test.simi('orig.txt', 'orig_self.txt', 'D:/xx.txt')
    def test_self2(self):
        test.simi('orig.txt', 'orig_self2.txt', 'D:/xx.txt')
    def test_self3(self):
        test.simi('orig.txt', 'orig_self3.txt', 'D:/xx.txt')
    def test_self4(self):
        test.simi('orig.txt', 'orig_self4.txt', 'D:/xx.txt')
    def test_self5(self):
        test.simi('orig.txt', 'orig_self5.txt', 'D:/xx.txt')
    def test_self6(self):
        test.simi('orig.txt', 'orig_self6.txt', 'D:/xx.txt')

    def test_self7(self):
        test.simi('orig.txt', 'orig_self7.txt', 'D:/xx.txt')

    def test_self8(self):
        test.simi('orig.txt', 'orig_self8.txt', 'D:/xx.txt')
    def test_self9(self):
        test.simi('orig.txt', 'orig_self9.txt', 'D:/xx.txt')

    def test_self10(self):
        test.simi('orig.txt', 'orig_self10.txt', 'D:/xx.txt')
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestForAllText('test_add'))
    suite.addTest(TestForAllText('test_del'))
    suite.addTest(TestForAllText('test_dis_1'))
    suite.addTest(TestForAllText('test_dis_3'))
    suite.addTest(TestForAllText('test_dis_7'))
    suite.addTest(TestForAllText('test_dis_10'))
    suite.addTest(TestForAllText('test_dis_15'))
    suite.addTest(TestForAllText('test_mix'))
    suite.addTest(TestForAllText('test_rep'))
    suite.addTest(TestForAllText('test_self'))
    suite.addTest(TestForAllText('test_self2'))
    suite.addTest(TestForAllText('test_self3'))
    suite.addTest(TestForAllText('test_self4'))
    suite.addTest(TestForAllText('test_self5'))
    suite.addTest(TestForAllText('test_self6'))
    suite.addTest(TestForAllText('test_self7'))
    suite.addTest(TestForAllText('test_self8'))
    suite.addTest(TestForAllText('test_self9'))
    suite.addTest(TestForAllText('test_self10'))
    runner = BeautifulReport(suite)

    runner.report(
        description='论文查重测试报告',  # => 报告描述
        filename='nlp_TFIDF.html',  # => 生成的报告文件名
        log_path='.'  # => 报告路径
    )