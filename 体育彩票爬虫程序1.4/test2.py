import requests
import time
from lxml import etree


headers = {
    'User-Agent': 'Baiduspider'
}
current_time_ticks = time.time()

def get_html(url):
    while True:
        try:
            response = requests.get(url, headers=headers)
            break
        except:
            print('爬取失败')
            time.sleep(1)
    response.encoding = 'GBK'
    html = response.text
    return html


def parse_html(html):
    global current_time_ticks
    klfc1 = []
    klfc2 = []
    klfc3 = []
    klfc4 = []
    klfc5 = []
    klfc6 = []
    etree_html = etree.HTML(html)
    tds = etree_html.xpath('//table[@id="datatb"]/tr')
    format = '%Y-%m-%d %H:%M:%S'
    for td in tds:
        update_time = td.xpath('./@data-time')[0]
        update_time_ticks = time.mktime(time.strptime(update_time, format))
        diff_time = current_time_ticks - update_time_ticks
        if diff_time >= 3600:
            continue
        all_data = td.xpath('.//td[3]//@klfc')
        klfc1.append(float(all_data[0]))
        klfc2.append(float(all_data[1]))
        klfc3.append(float(all_data[2]))
        klfc4.append(float(all_data[3]))
        klfc5.append(float(all_data[4]))
        klfc6.append(float(all_data[5]))
    if not klfc1:
        data = ''
    else:
        data = '      '.join([str(i) for i in [round(sum(klfc1) / len(klfc1), 2),
                                               round(sum(klfc2) / len(klfc2), 2),
                                               round(sum(klfc3) / len(klfc3), 2),
                                               round(sum(klfc4) / len(klfc4), 2),
                                               round(sum(klfc5) / len(klfc5), 2),
                                               round(sum(klfc6) / len(klfc6), 2)]])
    return data




def main():
    url = 'https://odds.500.com/fenxi/ouzhi-943391.shtml?ctype=3'
    html = get_html(url)
    parse_html(html)


if __name__ == '__main__':
    main()