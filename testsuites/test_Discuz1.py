from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_base import *
import unittest
import  time

class Discuz1(BaseTestCase):

    def test_Discuz1_login(self):
        login=login_Page(self.driver)
        login.open_url("http://127.0.0.1:8086/upload/forum.php")

        login.login1("czm","czm3292348")
        time.sleep(3)

    # def test_Discuz1_morenbankuai(self):
        morenbankuai=morenbankuai_page(self.driver)
        morenbankuai.morenbankuai1()

    # def test_Discuz1_fatie(self):
        fatie= fatie_page(self.driver)
        fatie.fatie1("王媛","王媛真是大沙雕")
        time.sleep(3)


    # def test_Discuz1_huifu(self):
        huifu=huifu_page(self.driver)
        huifu.huifu1("你说的对")


    # def test_Disuz1_tuichu(self):
        tuichu=tuichu_page(self.driver)
        tuichu.tuichu1()





if __name__ == "__main__":
    unittest.main()

