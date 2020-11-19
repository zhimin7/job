import requests
import time
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'referer': 'https://odds.500.com/fenxi/yazhi-920673.shtml',
    'x-requested-with': 'XMLHttpRequest'
}


def get_html(url):
    while True:
        try:
            response = requests.get(url, headers=headers)
            break
        except:
            time.sleep(1)
            print('爬取数据失败')
    response.encoding = 'GBK'
    result = response.json()
    return result


def parse_html(result):
    try:
        data = '      '.join(etree.HTML(result[0]).xpath('.//text()')).replace('       ', '')
    except:
        data = ''
    return data

def main():
    url = 'https://odds.500.com/fenxi1/inc/yazhiajax.php?fid=920673&id=280'
    result = get_html(url)
    data = parse_html(result)
    print(data)



if __name__ == '__main__':
    main()