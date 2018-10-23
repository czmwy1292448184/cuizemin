from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_base import *
import unittest
import  time


class Discuz2(BaseTestCase):

    def test_Discuz2_login(self):
        login2=login_Page(self.driver)

        login2.open_url("http://127.0.0.1:8086/upload/forum.php")

        login2.login1("admin","admin")
        time.sleep(3)

    # def test_Discuz2_morenbankuai(self):
        morenbankuai=morenbankuai_page(self.driver)
        morenbankuai.morenbankuai1()


    #
    # def test_Discuz2_shanchu(self):
        shanchu=shanchu_page(self.driver)
        shanchu.shanchu1()
        time.sleep(3)

    # def test_Discus2_bankuaiguanli(self):
        bankuaiguanli=bankuaiguanli_page(self.driver)
        bankuaiguanli.bankuaiguanli1("admin")

    # def test_Discuz2_tianjiabankuai(self):
        tianjiabankuai=tianjiabankuai_page(self.driver)
        tianjiabankuai.tianjiabankuai1("崔泽敏的版块")
    #
    # def test_Discuz2_login2(self):
        login2 = login_Page(self.driver)
        login2.login1("czm", "czm3292348")
        time.sleep(3)


    # def  test_Discuz2_xinbankuai(self):
        xinbankuai=xinbankuai_page(self.driver)
        xinbankuai.xinbankuai1()

    # def test_Discuz2_fatie(self):
        fatie2 = fatie_page(self.driver)
        fatie2.fatie1("王媛hahahahah", "王媛真是大沙雕hahahahah")
        time.sleep(3)

    # def test_Discuz2_huifu(self):
        huifu2 = huifu_page(self.driver)
        huifu2.huifu1("你说的对hahahahaha")

