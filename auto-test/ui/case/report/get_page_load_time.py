# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from ui.util.DriverInit import DriverInit
import time


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        Options = webdriver.ChromeOptions()
        Options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=Options)
        # self.driver = webdriver.Chrome()
        self.driver = DriverInit().driver
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.img = """           // 首屏图片加载完成 
                            let mytiming = window.performance.timing;
                            return window.lastImgLoadTime - mytiming.navigationStart ;
                """
        self.intfaces = """   https://blog.csdn.net/weixin_42284354/article/details/80416157
        // 接口完成加载完成 
                            let mytiming = window.performance.timing;
                            return Report.SPEED.LASTCGI - mytiming.navigationStart ;
                """
        self.DNS = """          // DNS查询耗时 
                    let mytiming = window.performance.timing;
                    return mytiming.domainLookupEnd - mytiming.domainLookupStart ;
        """
        self.TCP = """          // TCP链接耗时 
                    let mytiming = window.performance.timing;
                    return mytiming.connectEnd - mytiming.connectStart ;
        """
        self.request = """          // request请求耗时 
                    let mytiming = window.performance.timing;
                    return mytiming.responseEnd  - mytiming.responseStart ;
        """
        self.dom = """          //  解析dom树耗时 
                    let mytiming = window.performance.timing;
                    return mytiming.domComplete - mytiming.domInteractive ;
        """
        self.Ari = """          // 白屏时间 
                    let mytiming = window.performance.timing;
                    return mytiming.responseStart - mytiming.navigationStart ;
        """

        self.domready = """          // domready时间 
                    let mytiming = window.performance.timing;
                    return mytiming.domContentLoadedEventEnd   - mytiming.fetchStart ;
        """
        self.loadEventTime = """
                   let mytiming = window.performance.timing;
                   return mytiming.loadEventEnd - mytiming.navigationStart ;
                      """
        self.gather_data_dict = [
            {'UrlName': 'xiaoiron',
             'Url': 'https://www.baidu.com/',
             'number': 20}
        ]
        # 添加压测网址，在数组汇总添加一个 Dict即可
        self.gather_data_dict_ = [
            {'UrlName': '首页',
             'Url': 'http://zs.cnknowledge.com/',
             'number': 20},
            {'UrlName': '政策法规',
             'Url': 'http://zs.cnknowledge.com/html/policy_Law/law_know.html?parentId=3&type=1',
             'number': 20},
            {'UrlName': '行业新闻',
             'Url': 'http://zs.cnknowledge.com/html/trade_News/news_pages.html?parentId=1&type=2',
             'number': 20},
            {'UrlName': '学术前言',
             'Url': 'http://zs.cnknowledge.com/html/study_Leading/study_news.html?parentId=2&type=3',
             'number': 20},
            {'UrlName': '专题报道',
             'Url': 'http://zs.cnknowledge.com/html/special_report/report_event.html?parentId=4&type=4',
             'number': 20},
            {'UrlName': '名录',
             'Url': 'http://zs.cnknowledge.com/html/list_new/organization.html?parentId=5&type=5',
             'number': 20}
        ]

    def test_untitled_test_case(self):
        # 返回结果
        result = []
        # 读取压测数数据，返回加载结果！
        for data in self.gather_data_dict:
            result_temp = {
                "UrlName": data["UrlName"],
                "Url": data["Url"],
                "number": data["number"],
                "NoCache": self.__get_page_load_time_NoCache(data['Url'], data['number']),
                "Cache": self.__get_page_load_time_Cache(data['Url'], data['number'])
            }
            result.append(result_temp)
        print(result)

    def __get_page_load_time_NoCache(self, Url, number=1):
        """
        网页无缓存的情况下进行加载速度测试
        :param Url: 加载的网址
        :param number: 加载次数
        :return:
        """
        driver = self.driver
        page = []
        domready = []
        res_page = {}
        res_domready = {}
        for i in range(number):
            # 调用浏览器打开一个新窗口
            driver.execute_script("window.open('','_blank');")
            # 窗口定位到新打开的窗口
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(Url)
            page.append(int(driver.execute_script(self.loadEventTime)))
            domready.append(int(driver.execute_script(self.domready)))
            time.sleep(0.5)
            # 关闭窗口
            driver.execute_script("window.close();")
            # 窗口定位返回旧窗口
            driver.switch_to.window(driver.window_handles[-1])

        res_page['max'] = max(page)
        res_page['min'] = min(page)
        res_page['avg'] = sum(page) / len(page)
        print(res_page)
        res_domready['max'] = max(domready)
        res_domready['min'] = min(domready)
        res_domready['avg'] = sum(domready) / len(domready)

        return {"页面加载时间": res_page,
                "DOM加载时间": res_domready}

    def __get_page_load_time_Cache(self, Url, number=5):
        """
        网页有缓存的情况下进行加载速度测试
        :param Url: 加载的网址
        :param number: 加载次数
        :return:
        """
        driver = self.driver
        page = []
        domready = []
        res_page = {}
        res_domready = {}
        driver.get(Url)
        for i in range(number):
            driver.get(Url)
            page.append(int(driver.execute_script(self.loadEventTime)))
            domready.append(int(driver.execute_script(self.domready)))

        res_page['max'] = max(page)
        res_page['min'] = min(page)
        res_page['avg'] = sum(page) / len(page)

        res_domready['max'] = max(domready)
        res_domready['min'] = min(domready)
        res_domready['avg'] = sum(domready) / len(domready)

        return {"页面加载时间": res_page,
                "DOM加载时间": res_domready}

    def tearDown(self):
        pass


if __name__ == '__main__':
    result = [{'UrlName': 'baidu', 'Url': 'https://www.baidu.com/', 'number': 3,
               'NoCache': {'页面加载时间': {'max': 523, 'min': 284, 'avg': 400.6666666666667},
                           'DOM加载时间': {'max': 439, 'min': 256, 'avg': 348.6666666666667}},
               'Cache': {'页面加载时间': {'max': 131, 'min': 129, 'avg': 130.0},
                         'DOM加载时间': {'max': 101, 'min': 85, 'avg': 94.0}}}]

    for re in result:
        print(re["UrlName"])
        print(re["Url"])
        Cache_page = re["Cache"]['页面加载时间']
        Cache_dom = re["Cache"]['DOM加载时间']
        NoCache_page = re["NoCache"]['页面加载时间']
        NoCache_dom = re["NoCache"]['DOM加载时间']
        print(Cache_page["max"], Cache_page["min"], Cache_page["avg"], Cache_dom["max"], Cache_dom["min"],
              Cache_dom["avg"])
        print(NoCache_page["max"], NoCache_page["min"], NoCache_page["avg"], NoCache_dom["max"], NoCache_dom["min"],
              NoCache_dom["avg"])