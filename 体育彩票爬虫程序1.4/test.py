import requests
import time
from lxml import etree


headers = {'User-Agent': 'Baiduspider'}
current_time_ticks = time.time()
# response = requests.get(url, headers=headers)
# response.encoding = 'GBK'
# html = response.text


def exchange(url):
    while True:
        try:
            response = requests.get(url, headers=headers)
            break
        except:
            time.sleep(1)
            print('获取数据失败')
    response.encoding = 'GBK'
    html = response.text
    with open('主流公司.html', 'w', encoding='GBK') as f:
        f.write(html)
    # return response.text
    print('爬取完毕')


def read_html():
    # html = open('主流公司.html', 'r')
    # return html
    with open('主流公司.html', 'r') as f:
        html = f.read()
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
    # print(tds)
    for td in tds:
        update_time = td.xpath('./@data-time')[0]

        format = '%Y-%m-%d %H:%M:%S'
        update_time_ticks = time.mktime(time.strptime(update_time, format))
        if current_time_ticks - update_time_ticks >= 3600*3:
            continue
        all_data = td.xpath('.//td[3]//@klfc')
        klfc1.append(float(all_data[0]))
        klfc2.append(float(all_data[1]))
        klfc3.append(float(all_data[2]))
        klfc4.append(float(all_data[3]))
        klfc5.append(float(all_data[4]))
        klfc6.append(float(all_data[5]))
    print(klfc1)
    print(klfc2)
    print(klfc3)
    print(klfc4)
    print(klfc5)
    print(klfc6)
    data = '      '.join([str(i) for i in [round(sum(klfc1) / len(klfc1), 2),
                                     round(sum(klfc2) / len(klfc2), 2),
                                     round(sum(klfc3) / len(klfc3), 2),
                                     round(sum(klfc4) / len(klfc4), 2),
                                     round(sum(klfc5) / len(klfc5), 2),
                                     round(sum(klfc6) / len(klfc6), 2)]])
    return data









def main():
    # url = 'https://odds.500.com/fenxi/ouzhi-961984.shtml?ctype=2'
    # exchange(url)
    html = read_html()
    # print(html)
    data = parse_html(html)
    print(data)


if __name__ == '__main__':
    main()
