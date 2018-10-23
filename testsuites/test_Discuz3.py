from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_base import *
import unittest
import  time


class Discuz3(BaseTestCase):

    def test_Discuz3_login(self):
        login3=login_Page(self.driver)
        login3.open_url("http://127.0.0.1:8086/upload/forum.php")
        login3.login1("czm","czm3292348")
        time.sleep(3)

    # def test_Discuz3_sousuotiezi(self):
        tiezisousuo=tiezisousuo_page(self.driver)
        tiezisousuo.tiezisousuo1("王媛")

    # def test_Discuz3_tuichu(self):
        tuichu3=tuichu_page(self.driver)
        tuichu3.tuichu1()