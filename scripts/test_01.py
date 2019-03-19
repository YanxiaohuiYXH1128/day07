import os
import sys

import pytest

sys.path.append(os.getcwd())

import allure


class Test01:
    @allure.step("001方法被执行")
    def test001(self):
        allure.attach("点击新增地址按钮","")
        print("001被执行")


    @allure.step("002方法被执行")
    def test002(self):
        print("002被执行")

    # 失败截图并写入报告
    @allure.severity("RITICAL")
    def test003(self):
        print("断言失败,截图并写入报告")
        with open("./image/faile.png","rb") as f:
            allure.attach("失败原因",f.read(),allure.attach_type.PNG)
            assert False