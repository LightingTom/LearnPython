import re
from html.parser import HTMLParser
from urllib.request import urlopen, Request


def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    req = Request(url, headers=headers)
    with urlopen(req, timeout=25) as f:
        data = f.read()
        print(f'Status: {f.status} {f.reason}')
        print()
    return data.decode("utf-8")


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parsedata = ''  # 设置一个空的标志位
        self.info = []

    def handle_starttag(self, tag, attrs):
        if ('class', 'sky skyid lv3') in attrs:
            self.__parsedata = 'date'
        if ('class', 'wea') in attrs:
            self.__parsedata = 'weather'
        if ('class', 'tem') in attrs:
            self.__parsedata = 'temperature'
        if ('class', 'win') in attrs:
            self.__parsedata = 'wind'

    def handle_endtag(self, tag):
        self.__parsedata = ''  # 在HTML 标签结束时，把标志位清空

    def handle_data(self, data):

        if self.__parsedata == 'date':
            # 通过标志位判断，输出打印标签内容
            self.info.append(f'日期:{data}')

        if self.__parsedata == 'weather':
            self.info.append(f'天气:{data}')

        if self.__parsedata == 'temperature':
            self.info.append(f'气温：{data}')

        if self.__parsedata == 'windlevel':
            self.info.append(f'风力：{data}')


def main():
    parser = MyHTMLParser()
    URL = 'http://www.weather.com.cn/weather/101280601.shtml'
    data = get_data(URL)
    parser.feed(data)
    for s in parser.info:
        print(s)


if __name__ == '__main__':
    main()
