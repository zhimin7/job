import time

import requests
import xlwt
from lxml import etree

headers = {
    'user-agent': 'Baiduspider'
}

def proxy():
    url = 'http://guzhimin.v4.dailiyun.com/query.txt?key=NP02CA4A1D&word=&count=&rand=true&detail=true'
    result = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})

    # print(result.text.split(":")[0])
    proxyaddr = result.text.split(":")[0]  # 代理IP地址
    proxyport = 57114  # 代理IP端口
    proxyusernm = "guzhimin"  # 代理帐号
    proxypasswd = "68410As"  # 代理密码
    proxyurl = "http://" + proxyusernm + ":" + proxypasswd + "@" + proxyaddr + ":" + "%d" % proxyport
    proxies = {'http': proxyurl, 'https': proxyurl}
    return proxies

def paesrMatchList():
    # 获取比赛列表
    TTT = time.strftime('%Y-%m-%d %H时%M分', time.localtime())
    workbook = xlwt.Workbook(encoding="utf-8")
    sheet = workbook.add_sheet(f'500彩票-{TTT}')
    list_ = ['home_team', 'score', 'away_team', 'handicap', 'all_companies', 'mainstream_companines',
             'exchange', 'BF']
    for i in range(len(list_)):
        sheet.write(0, i, list_[i])

    url = 'https://live.500.com/zqdc.php'
    while True:
        try:
            result = requests.get(url, headers=headers, timeout=5)
            break
        except:
            time.sleep(1)
            print("--paesrMatchList--")
    result.encoding = 'GBK'
    n = 0
    for ii in etree.HTML(result.text).xpath("//table[@id='table_match']/tbody/tr"):
        temp = {}
        temp['matchname'] = ii.xpath("./td[2]//text()")[0]
        temp['id'] = ii.xpath("@fid")
        temp['Time'] = ii.xpath("./td[4]//text()")[0].replace("\xa0", " ")
        temp["H"] = "".join(ii.xpath("./td[6]//text()"))  # 主队
        temp["L"] = "".join(ii.xpath("./td[8]//text()"))  # 客队
        temp['score'] = "".join(ii.xpath("./td[7]//a[2]/text()"))  # 比分
        temp["T"] = ii.xpath("./td[5]//text()")[0].replace("\xa0", "")
        print(temp)
        temp['klfc'] = klfcAll(temp)
        temp['bifa'], temp['jiaoyi'] = jiaoyiklfc(temp)
        temp['zhuliu'] = zhuliuklfc(temp)
        temp['huangguan'] = yazhi(temp)
        print(temp)
        sheet.write(n + 1, 0, temp['H'])
        sheet.write(n + 1, 1, temp['score'])
        sheet.write(n + 1, 2, temp['L'])
        sheet.write(n + 1, 3, temp['huangguan'])
        sheet.write(n + 1, 4, temp['klfc'])
        sheet.write(n + 1, 5, temp['zhuliu'])
        sheet.write(n + 1, 6, temp['jiaoyi'])
        sheet.write(n + 1, 7, temp['bifa'])
        workbook.save(f'500彩票-{TTT}.xls')
        n += 1


def klfcAll(temp):
    # 全部公司离散值
    url = f'https://odds.500.com/fenxi/ouzhi-{temp["id"]}.shtml?ctype=1'
    while True:
        try:
            result = requests.get(url, headers=headers, timeout=5)
            break
        except:
            time.sleep(1)
            print("--klfcAll--")
    result.encoding = 'GBK'
    klfc = ",   ".join(etree.HTML(result.text).xpath("//td[contains(text(),'离散值')]/../td[2]//tr/td/text()"))
    return klfc


def jiaoyiklfc(temp):
    # 交易所离散值
    url = f'https://odds.500.com/fenxi/ouzhi-{temp["id"]}.shtml?ctype=3'
    while True:
        try:
            result = requests.get(url, headers=headers, timeout=5)
            break
        except:
            time.sleep(1)
            print("--jiaoyiklfc--")
    result.encoding = 'GBK'
    bifa = ",   ".join(etree.HTML(result.text).xpath("//td[contains(@title,'必发')]/../td[3]//@klfc"))  # 必发离散值
    klfc1 = []
    klfc2 = []
    klfc3 = []
    klfc4 = []
    klfc5 = []
    klfc6 = []
    for ii in etree.HTML(result.text).xpath("//table[@id='datatb']/tr"):
        if ii.xpath("./td[2]/@title")[0] == "Redbet":
            continue
        Dlist = ii.xpath(".//td[3]//@klfc")
        klfc1.append(float(Dlist[0]))
        klfc2.append(float(Dlist[1]))
        klfc3.append(float(Dlist[2]))
        klfc4.append(float(Dlist[3]))
        klfc5.append(float(Dlist[4]))
        klfc6.append(float(Dlist[5]))
    if not klfc1:
        jiaoyi = ""
    else:
        jiaoyi = ",   ".join([str(i) for i in [round(sum(klfc1) / len(klfc1), 2), round(sum(klfc2) / len(klfc2), 2),
                                            round(sum(klfc3) / len(klfc3), 2),round(sum(klfc4) / len(klfc4), 2),
                                            round(sum(klfc5) / len(klfc5), 2), round(sum(klfc6) / len(klfc6), 2)]])
    return bifa, jiaoyi


def zhuliuklfc(temp):
    # 主流公司离散值
    url = f'https://odds.500.com/fenxi/ouzhi-{temp["id"]}.shtml?ctype=2'
    while True:
        try:
            result = requests.get(url, headers=headers, timeout=5)
            break
        except:
            time.sleep(1)
            print("--zhuliuklfc--1")
    result.encoding = 'GBK'
    klfc1 = []
    klfc2 = []
    klfc3 = []
    klfc4 = []
    klfc5 = []
    klfc6 = []
    for ii in etree.HTML(result.text).xpath("//table[@id='datatb']/tr"):
        id = ii.xpath("./@id")[0]
        headers['referer'] = url
        infourl = f'https://odds.500.com/fenxi1/json/ouzhi.php?fid={temp["id"]}&cid={id}'
        while True:
            try:
                response = requests.get(infourl, headers=headers, timeout=5).json()
                break
            except:
                time.sleep(1)
                print("--zhuliuklfc--2")
        timeArray = time.strptime(response[0][4], "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        if int(time.time()) - timeStamp > 3600 * 3:
            continue
        Dlist = ii.xpath(".//td[3]//@klfc")
        klfc1.append(float(Dlist[0]))
        klfc2.append(float(Dlist[1]))
        klfc3.append(float(Dlist[2]))
        klfc4.append(float(Dlist[3]))
        klfc5.append(float(Dlist[4]))
        klfc6.append(float(Dlist[5]))
    if not klfc1:
        zhuliu = ""
    else:
        zhuliu = ",   ".join([str(i) for i in [round(sum(klfc1) / len(klfc1), 2), round(sum(klfc2) / len(klfc2), 2),
                                            round(sum(klfc3) / len(klfc3), 2), round(sum(klfc4) / len(klfc4), 2),
                                            round(sum(klfc5) / len(klfc5), 2), round(sum(klfc6) / len(klfc6), 2)]])
    return zhuliu

z`
def yazhi(temp):
    headers = {
        'referer': f'https://odds.500.com/fenxi/yazhi-{temp["id"]}.shtml',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    url = f'https://odds.500.com/fenxi1/inc/yazhiajax.php?fid={temp["id"]}&id=280'
    while True:
        try:
            result = requests.get(url, headers=headers, timeout=5).json()
            break
        except:
            time.sleep(1)
            print("--yazhi--")
    try:
        huangguan = ",   ".join(etree.HTML(result[0]).xpath(".//text()")).replace(" ", "")
    except:
        huangguan = ""
    return huangguan


if __name__ == '__main__':
    paesrMatchList()
