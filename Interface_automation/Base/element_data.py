# 数据处理
# 读取json数据的公用函数
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions




def web_ele(get_url="https:www.baidu.com"):
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = Chrome(options=option)
    driver.maximize_window()
    driver.get(get_url)
    return driver


class driver_utils():

    def __init__(self, driver=web_ele(get_url="https:www.baidu.com")):
        self.driver = driver

    def build_data(self, filename):
        """
        类似于一个接口，可以通过准备好的json参数执行多个用例
        :param filename:
        :return:
        """
        # 存储数据空列表
        case_data = []
        # 1 .打开json文件
        with open(file=filename, encoding='utf-8') as f:
            # 2.读取所有的json数据
            dict_str = json.load(f)
            # 3.遍历第一层的键值
            for i in dict_str.values():
                # 4.一次性获取字典的所有键值以列表形式呈现
                a = list(i.values())
                # 5.获取到键值的列表需要进行存储
                case_data.append(a)
            # 6.返回读取并组织好的数据提供给测试用例进行使用
            return case_data

    def driver_element(self, code: str, text: str = None):
        """
        增加显示等待，并判断文本元素是否存在,如果找的到元素则返回元素对象,找不到则返回False
        :param code: 校验使用的元素定位方式，预设值：xpath_text、id、class、element_xpath、element_css_selector、elements_css_selector、elements_class、elements_xpath
        :param text: element元素
        :return:
        """
        try:
            if code == "xpath_text":
                element = WebDriverWait(self.driver, 8, 0.5).until(
                    lambda x: x.find_element_by_xpath(xpath="//*[contains(text(),'{}')]".format(text)))
                print(
                    f"定位方式:{code};  element元素:{text};  元素标签:{element.tag_name};  元素内容:{element.text};")
                return element
            elif code == "id":
                element = WebDriverWait(self.driver, 8, 0.5).until(
                    lambda x: x.find_element_by_id(text))
                print(
                    f"定位方式:{code};  element元素:{text};  元素标签:{element.tag_name};  元素内容:{element.text};")
                return element
            elif code == "class":
                element = WebDriverWait(self.driver, 8, 0.5).until(
                    lambda x: x.find_element_by_class(text))
                print(f"定位方式:{code};  element元素:{text};  元素标签:{element.tag_name};  元素内容:{element.text};")
                return element
            elif code == "element_xpath":
                element = WebDriverWait(self.driver, 8, 0.5).until(
                    lambda x: x.find_element_by_xpath(text))
                print(f"定位方式:{code};  element元素:{text};  元素标签:{element.tag_name};  元素内容:{element.text};")
                return element
            elif code == "element_css_selector":
                element = WebDriverWait(self.driver, 8, 0.5).until(
                    lambda x: x.find_element_css_selector(text))
                print(f"定位方式:{code};  element元素:{text};  元素标签:{element};  元素内容:{element.text};")
                return element
            elif code == "elements_css_selector":
                element = WebDriverWait(self.driver, 8, 0.5).until(
                    lambda x: x.find_elements_css_selector(text))
                print(f"定位方式:{code};  element元素:{text};  元素集合:{element};  元素内容:{element};")
                return element
            elif code == "elements_class":
                element = WebDriverWait(self.driver, 8, 0.5).until(
                    lambda x: x.find_elements_by_class(text))
                print(f"定位方式:{code};  element元素:{text};  元素集合:{element};  元素内容:{element};")
                return element
            elif code == "elements_xpath":
                element = WebDriverWait(self.driver, 8, 0.5).until(
                    lambda x: x.find_elements_by_xpath(text))
                print(f"定位方式:{code};  element元素:{text};  元素集合:{element};  元素内容:{element};")
                return element
            else:
                element = "校验码错误！"
                print(element)

        except Exception as e:
            print("定位不到元素或提取不到元素的内容", f"异常类型：{repr(e).replace('Error', ' Error;  异常内容:')}")

    def driver_quit(self):
        self.driver.quit()

    def java_script(self, script_text:str, *args):
        """
        :param script_text:要执行的js代码
        :return:
        """
        js = self.driver.execute_script(script=script_text)
        print(f"js代码:{js};  执行内容:{script_text}")
        return js


if __name__ == '__main__':
    # driver = driver_utils()
    # driver.driver_element("id", "kw").send_keys("国家兴亡，匹夫有责")
    # driver.driver_element("id", "su").click()
    # time.sleep(5)
    # driver.java_script('alert("恭喜你..........")')
    # driver.driver_quit()
    pass

# return rets[0] if rets else default
