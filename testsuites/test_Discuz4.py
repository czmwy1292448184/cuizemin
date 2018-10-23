from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_base import *
import unittest
import  time

class Discuz4(BaseTestCase):

    def test_Discuz4_login(self):
        login4=login_Page(self.driver)
        login4.open_url("http://127.0.0.1:8086/upload/forum.php")
        login4.login1("czm","czm3292348")
        time.sleep(3)

    # def test_Discuz_morenbankuai(self):
        morenbankuai4=morenbankuai_page(self.driver)
        morenbankuai4.morenbankuai1()

    # def test_Discuz4_toupiaoyemian(self):
        toupiaoyemian4=toupiaoyemian_page(self.driver)
        toupiaoyemian4.toupiaoyemian1()

    # def test_Discuz_faqitoupiao(self):
        faqitoupiao=faqitoupiao_page(self.driver)
        faqitoupiao.faqitoupiao1("测试班谁最丑","郭荣鑫","小花","小李")

    # def test_Discuz_toupiao(self):
        toupiao=toupiao_page(self.driver)
        toupiao.toupiao1()

        toupiao_print=toupiao_print_page(self.driver)
        toupiao_print.toupiao_print1()

