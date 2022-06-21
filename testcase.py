from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from appium.webdriver.extensions.android.nativekey import AndroidKey
from app_information import desired_caps  # 导入被测试app的信息
import uiautomator2
import unittest
import time
import re

case_result = '/Users/yuanxinming/Desktop/everday/reslut.html'

# case 条数
casenumber = 0


class DBhome(unittest.TestCase):

    # 连接Appium Server，初始化自动化环境
    def setUp(self) -> None:
        self.driver = webdriver.Remote('http://192.168.18.231:4723/wd/hub', desired_caps)
        # 设置缺省等待时间
        self.driver.implicitly_wait(20)
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert = True  # 是否继续接受下一个警告#

    # 检查首页特色功能模块展示正确
    def test01_Featuresmodule(self, uiauto2=uiautomator2):

        try:
            driver = self.driver
            global casenumber
            casenumber += 1

            uiauto2 = uiauto2.connect_usb('PQY5T20A14007047')
            uiauto2.app_start('com.dangbei.remotecontroller')

        except:
            raise Exception('app启动失败')

            print(f'------------------开始执行case{casenumber}-----------------------')

        try:
            # 检查首页特色功能模块tittle展示正确
            driver.implicitly_wait(10)
            features = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.'
                                                     'LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]')

            # 检查特色功能模块的遥控器tab展示正确
            driver.implicitly_wait(3)
            The_remote_control = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout'
                                                               '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')

            # 检查特色功能模块的魔法同屏tab展示正确
            driver.implicitly_wait(3)
            magic = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.'
                                                  'widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')

            # 检查特色功能模块远程看家tab展示正确
            driver.implicitly_wait(3)
            Remote_guarding = driver.find_element(By.XPATH,
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]'
                                                  '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView')

            # 检查特色模块的视频电话tab展示正确
            driver.implicitly_wait(3)
            Video_call = driver.find_element(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView'
                                             '/android.view.ViewGroup[4]/android.widget.TextView')

        except:

            raise Exception('首页特色功能模块元素获取失败')

        try:
            if features and The_remote_control and magic and Remote_guarding and Video_call:
                with open(case_result, 'w') as result1:
                    driver.implicitly_wait(5)
                    result1.write(f"case:{casenumber}首页特色功能模块展示正确\n")
                    print("首页特色功能模块展示正确")
                    result1.close()
            else:
                with open(case_result, 'w') as result1:
                    driver.implicitly_wait(5)
                    result1.write(f"case:{casenumber}首页特色功能模块展示错误\n")
                    print("首页特色功能模块展示错误")
                    result1.close()

        except:

            raise Exception('首页特色功能模块展示错误，请检查')
            with open(case_result, 'w') as result1:
                driver.implicitly_wait(5)
                result1.write(f"case:{casenumber}首页特色功能模块遥控器、魔法同屏、远程看家、视频通话tab均跳转错误\n")
                print("首页特色功能模块遥控器、魔法同屏、远程看家、视频通话tab均跳转错误页面")
                result1.close()

        print(f'case{casenumber}、检查首页特色功能模块展示正确执行结束')

    # 检查首页特色功能模块遥控器、魔法同屏、远程看家、视频通话tab展示正确
    def test02_Featuresmodule_Lookatall(self, uiauto2=uiautomator2):

        try:
            driver = self.driver
            global casenumber
            casenumber += 1

            uiauto2 = uiauto2.connect_usb('PQY5T20A14007047')
            uiauto2.app_start('com.dangbei.remotecontroller')

        except:
            raise Exception('app启动失败')

            print(f'------------------开始执行case{casenumber}-----------------------')

        # 检查全部功能点存在，并且点击可以跳转正确页面
        # featuresallfunction 全部功能
        driver.implicitly_wait(10)
        featuresallfunction = driver.find_element(By.XPATH,
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/'
                                                  'androidx.recyclerview.widget.RecyclerView/android.view.'
                                                  'ViewGroup[1]/android.widget.TextView[2]')


        # 点击全部功能
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout'
                                      '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                      'android.widget.FrameLayout/android.widget.FrameLayout/androidx.'
                                      'viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.'
                                      'widget.RecyclerView/android.view.'
                                      'ViewGroup[1]/android.widget.TextView[2]').click()

        # 检查点击特色功能点击全部功能跳转页面正确
        # featuresfunction 特色功能title
        driver.implicitly_wait(5)
        featuresfunction = driver.find_element(By.XPATH,
                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                               'android.widget.FrameLayout/android.widget.LinearLayout/android.'
                                               'widget.FrameLayout/android.view.ViewGroup[1]/android.widget.'
                                               'RelativeLayout/android.widget.TextView[1]')

        try:
            if featuresfunction:
                with open(case_result, 'a') as result1:
                    driver.implicitly_wait(5)
                    result1.write(f"case:{casenumber}点击首页特色功能模块全部功能，跳转页面展示正确。\n")
                    print("点击首页特色功能模块全部功能，跳转页面展示正确。")
                    result1.close()
            else:
                with open(case_result, 'a') as result1:
                    driver.implicitly_wait(5)
                    result1.write(f"case:{casenumber}点击首页特色功能模块全部功能，跳转页面展示错误\n")
                    print("点击首页特色功能模块全部功能，跳转页面错误。")
                    result1.close()

        except:

            with open(case_result, 'a') as result1:
                driver.implicitly_wait(5)
                result1.write(f"case:{casenumber}点击首页特色功能模块全部功能，跳转页面展示错误\n")
                print("点击首页特色功能模块全部功能，跳转页面错误。")
                result1.close()

        print(f'case{casenumber}、检查首页特色功能模块，点击更多功能跳转页面用例执行结束')

    # 检查首页特色功能模块遥控器、视频通话tab均跳转正确页面
    def test03_Featuresmodule_tabfind(self, uiauto2=uiautomator2):
            try:
                driver = self.driver
                global casenumber
                casenumber += 1

                uiauto2 = uiauto2.connect_usb('PQY5T20A14007047')
                uiauto2.app_start('com.dangbei.remotecontroller')

            except:
                raise Exception('app启动失败')

                print(f'------------------开始执行case{casenumber}-----------------------')

            try:
                # 检查首页找回遥控器tab点击后可以跳转正确页面
                driver.implicitly_wait(10)
                driver.find_element(By.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager'
                                    '.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.'
                                    'RecyclerView/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView/'
                                    'android.view.ViewGroup[1]/android.widget.TextView').click()

                # 检查点击遥控器tab跳转后页面正确
                driver.implicitly_wait(5)
                findTheremotecontrol = driver.find_element(By.XPATH,
                                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.w'
                                                           'idget.FrameLayout/android.view.ViewGroup[1]/android.widget.TextVi'
                                                           'ew[2]')
                # 返回首页操作
                driver.implicitly_wait(3)
                driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/and'
                                              'roid.widget.FrameLayout/android.view'
                                              '.ViewGroup[1]/android.widget.ImageView[1]').click()


                # 检查首页点击视频通话后可以跳转正确页面
                driver.implicitly_wait(3)
                driver.find_element(By.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView/android.view.V'
                                    'iewGroup[4]/android.widget.TextView').click()

                # 检查点击远程看家tab跳转后页面正确
                # 获取通话记录
                driver.implicitly_wait(3)
                FindVideocall1 = driver.find_element(By.XPATH,
                                                     '//androidx.appcompat.app.a.c[@content-desc="通话"]/android.widget.RelativeLayo'
                                                     'ut/androidx.appcompat.widget.Linear'
                                                     'LayoutCompat/android.widget.TextView')
                # 获取亲友圈title文案
                driver.implicitly_wait(15)
                FindVideocall1 = driver.find_element(By.XPATH,
                                                     '//androidx.appcompat.app.a.c[@content-desc="亲友圈"]/android.widget.RelativeLayout/androidx.appc'
                                                     'ompat.widget.LinearLayoutCompat/android.widget.TextView')

            except:

                raise Exception('跳转页面和获取元素错误，请检查')

            try:

                if FindVideocall1 and FindVideocall1:
                    with open(case_result, 'a') as result1:
                        driver.implicitly_wait(5)
                        result1.write(f"case:{casenumber}首页特色功能模块遥控器、魔法同屏、远程看家、视频通话tab均跳转正确页面\n")
                        print("首页特色功能模块遥控器、魔法同屏、远程看家、视频通话tab均跳转正确页面")
                        result1.close()
                else:
                    with open(case_result, 'a') as result1:
                        driver.implicitly_wait(5)
                        result1.write(f"case:{casenumber}首页特色功能模块遥控器、魔法同屏、远程看家、视频通话tab均跳转错误\n")
                        print("首页特色功能模块遥控器、魔法同屏、远程看家、视频通话tab均跳转错误页面")
                        result1.close()

            except:

                raise Exception('判断跳转页面逻辑错误，请检查')
                with open(case_result, 'a') as result1:
                    driver.implicitly_wait(5)
                    result1.write(f"case:{casenumber}首页特色功能模块遥控器、魔法同屏、远程看家、视频通话tab均跳转错误\n")
                    print("首页特色功能模块遥控器、魔法同屏、远程看家、视频通话tab均跳转错误页面")
                    result1.close()

            print(f'case{casenumber}、检查首页特色功能模块遥控器、视频通话tab均跳正确用例执行完毕了')


