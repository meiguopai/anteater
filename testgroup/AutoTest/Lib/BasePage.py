#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : 
from PIL import Image
from pytesseract import pytesseract
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    """

    # 初始化driver、url、pagetitle等
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
    # __init__方法不能有返回值，只能返回None
    # self只实例本身，相较于类Page而言。
    def __init__(self, selenium_driver, base_url, pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle
        self.timeout = 30

    @staticmethod
    def browser(browser="Chrome"):
        """打开浏览器函数，Firefox，chrome，IE，phantomjs
           默认Chrome浏览器
        """
        try:
            if browser == "Chrome":
                driver = webdriver.Chrome()
                return driver
            elif browser == "firefox":
                driver = webdriver.Firefox()
                return driver
            elif browser == "IE":
                driver = webdriver.Ie()
                return driver
            elif browser == "phantomjs":
                driver = webdriver.PhantomJS()
                return driver
            else:
                print("找不到驱动")
        except Exception as msg:
            print("%s" % msg)

    # 通过title断言进入的页面是否正确。
    # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    def on_page_url(self, page_url):
        return page_url in self.driver.current_url

    # 打开页面，并校验页面链接是否加载正确
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
    def _open(self, url, pagetitle):
        # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
        assert self.on_page(pagetitle), u"打开页面失败 %s" % url

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url, self.pagetitle)
        self.driver.maximize_window()

    # 重写元素定位方法
    def find_element_by(self, *loc):
        #        return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            print(e)
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 重定义定位方法
    def find_elements(self, *element):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(element))
            return self.driver.find_elements(*element)
        except Exception as e:
            print(e)
            print("页面元素未能找到%s" % self, element)

    def base_open(self, url):
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)
        except Exception as e:
            print(e)

    # 定义close方法
    def close(self):
        try:
            self.driver.quit()
        except Exception as e:
            print(e)

    def find_element(self, name):
        try:
            element = self.driver.find_element_by_id(name)
        except Exception as e:
            try:
                element = self.driver.find_element_by_name(name)
            except Exception as e:
                try:
                    element = self.driver.find_element_by_xpath(name)
                except Exception as e:
                    try:
                        element = self.driver.find_element_by_css_selector(name)
                    except Exception as e:
                        try:
                            element = self.driver.find_element_by_class_name(name)
                        except Exception as e:
                            return None
        return element

    # 警告框
    def find_alert(self):
        try:
            alert = self.driver.switch_to_alert()
            alert.accept()
        except Exception as e:
            print(e)
            return None
        return alert

    def input(self, tag, value):
        e = self.find_element(tag)
        if e:
            e.clear()
            e.send_keys(value)
        else:
            print("Not found: " + tag)

    # 点击操作
    def click(self, element):
        alink = self.find_element(element)
        if alink:
            alink.click()
        else:
            print("Not found: " + element)

    def hrefClick(self, tag):
        xPathLink = "//a[contains(@href,'" + tag + "')]"
        self.click(xPathLink)

    def select(self, tag, option):
        e = self.find_element(tag)
        if e:
            Select(e).select_by_value(option)
        else:
            print("Not found: " + tag)

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        return self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 定义截图方法
    def capture_page(self, imgfile):
        self.driver.save_screenshot(imgfile)

    def parse_verifycode(self, imageElementId):
        try:
            self.driver.save_screenshot('../Data/vert.png')
            e = self.find_element(imageElementId)

            rangle = (int(e.location['x']), int(e.location['y']), \
                      int(e.location['x'] + e.size['width']), int(e.location['y'] + e.size['height']))

            Image.open('../Data/vert.png').crop(rangle).save('../Data/vc.png')
            vcode = pytesseract.image_to_string(Image.open('../Data/vc.png'), lang='eng')
            return vcode
        except Exception as e:
            print(e)

    def is_located(self, element, timeout=10):
        """判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(element))
        return result

    # --------------------------------------------------------------------------------------
    # 以下方法未验证
    def move_to_element(self, element):
        """
        鼠标悬停操作
        Usage:
        element = ("id","xxx")
        driver.move_to_element(element)
        """
        element = self.find_element(element)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        """
        浏览器返回窗口
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进下一个窗口
        """
        self.driver.forward()

    def close(self):
        """
        关闭浏览器
        """
        self.driver.close()

    def quit(self):
        """
        退出浏览器
        """
        self.driver.quit()

    def get_title(self):
        """获取title"""
        return self.driver.title

    def get_text(self, element):
        """获取文本"""
        element = self.find_element(element)
        return element.text

    def get_attribute(self, element, name):
        """获取属性"""
        element = self.find_element(element)
        return element.get_attribute(name)

    def js_execute(self, js):
        """执行js"""
        return self.driver.execute_script(js)

    def js_focus_element(self, element):
        """聚焦元素"""
        target = self.find_element(element)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滚动到底部"""
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, element, index):
        """通过索引,index是索引第几个，从0开始"""
        element = self.find_element(element)
        Select(element).select_by_index(index)

    def select_by_value(self, element, value):
        """通过value属性"""
        element = self.find_element(element)
        Select(element).select_by_value(value)

    def select_by_text(self, element, text):
        """通过文本值定位"""
        element = self.find_element(element)
        Select(element).select_by_value(text)

    def is_text_in_element(self, element, text, timeout=10):
        """判断文本在元素里，没定位到元素返回False，定位到元素返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(element, text))
        except TimeoutException:
            print("元素没有定位到:" + str(element))
            return False
        else:
            return result

    def is_text_in_value(self, element, value, timeout=10):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(element, text)
        :param element:
        :param value:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element_value(element, value))
        except TimeoutException:
            print("元素没定位到：" + str(element))
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        """判断title完全等于"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        """判断title包含"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, element, timeout=10):
        """判断元素被选中，返回布尔值"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(element))
        return result

    def is_selected_be(self, element, selected=True, timeout=10):
        """判断元素的状态，selected是期望的参数true/False
        返回布尔值"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_selection_state_to_be(element,
                                                                                                       selected))
        return result

    def is_alert_present(self, timeout=10):
        """判断页面是否有alert，
        有返回alert(注意这里是返回alert,不是True)
        没有返回False"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        return result

    def is_visibility(self, element, timeout=10):
        """元素可见返回本身，不可见返回Fasle"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(element))
        return result

    def is_invisibility(self, element, timeout=10):
        """元素可见返回本身，不可见返回True，没找到元素也返回True"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.invisibility_of_element_located(element))
        return result

    def is_clickable(self, element, timeout=10):
        """元素可以点击is_enabled返回本身，不可点击返回Fasle"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(element))
        return result