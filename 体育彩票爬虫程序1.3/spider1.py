import time
import xlwt
import requests
from lxml import etree
import threading


headers = {'User-Agent': 'Baiduspider'}

def parse_match_list():
    # 获取当前时间
    current_time = time.strftime('%Y-%m-%d %H时%M分', time.localtime())
    work_book = xlwt.Workbook(encoding='utf-8')
    sheet = work_book.add_sheet('500彩票')
    list_ = ['time', 'home_team', 'score', 'visting_team', 'All_companies',
     'mainstream_companines','BiFa', 'Matchbook', 'Leon']
    for i in range(len(list_)):
        sheet.write(0,i,list_[i])
    url = 'https://live.500.com/zqdc.php'
    while True:
        try:
            response = requests.get(url, headers=headers)
            break
        except Exception as e:
            print('500彩票列表获取失败，请稍等。。。')
    encode = response.apparent_encoding
    response.encoding = 'GBK'
    html = response.text
    # with open('500.html', mode='w', encoding='GBK') as f:
    #     f.write(html)
    # print('Save ok')
    tds = etree.HTML(html).xpath('//table[@id="table_match"]/tbody/tr')
    line = 0
    clo = 0
    for td in tds:
        temp = {}
        try:
            temp['fid'] = td.xpath("@fid")[0]
        except:
            continue
        temp['home_team'] = ''.join(td.xpath('./td[6]//text()'))
        temp['visting_team'] = ''.join(td.xpath('./td[8]//text()'))
        temp['time'] = ''.join(td.xpath('./td[4]//text()'))
        temp['score'] = ''.join(td.xpath('./td[7]//text()'))
        # print(temp)
        # try:
        temp['All_companies'] = all_companies(temp)
        temp['BiFa'] = exchange_bifa(temp)
        temp['Matchbook'] = exchange_Matchbook(temp)
        temp['Leon'] = exchange_leon(temp)
        # except:
        #     continue
        print(temp)
        sheet.write(line+1, clo, temp['time'])
        sheet.write(line+1, clo+1, temp['home_team'])
        sheet.write(line+1, clo+2, temp['score'])
        sheet.write(line+1, clo+3, temp['visting_team'])
        sheet.write(line+1, clo+4, temp['All_companies'])
        sheet.write(line+1, clo+5, temp['All_companies'])
        sheet.write(line+1, clo+6, temp['BiFa'])
        sheet.write(line+1, clo+7, temp['Matchbook'])
        sheet.write(line+1, clo+8, temp['Leon'])
        work_book.save(f'500彩票-{current_time}.xls')
        line+=1

        print('爬取完成')
        # print(temp['fid'])

# 全部公司了离散值
def all_companies(temp):

    url = f'https://odds.500.com/fenxi/ouzhi-{temp["fid"]}.shtml?ctype=1'
    while True:
        # 爬取次数
        number = 1
        try:
            response = requests.get(url,headers=headers, timeout=10)
            break
        except:
            time.sleep(1)
            print('全部公司离散值第{}次获取失败'.format(number))
            number += 1
    response.encoding = 'GBK'
    result = response.text
    etree_html = etree.HTML(result)
    data = '      '.join(etree_html.xpath("//td[contains(text(),'离散值')]/../td[2]//tr/td/text()"))
    return data

# 必发离散值
def exchange_bifa(temp):
    # 获取必发离散值
    url = f'https://odds.500.com/fenxi/ouzhi-{temp["fid"]}.shtml?ctype=3'
    while True:
        number = 1
        try:
            response = requests.get(url, headers=headers)
            break
        except:
            time.sleep(1)
            print('第{}次获取必发数据失败'.format(number))
            number += 1
    response.encoding = 'GBK'
    result = response.text
    etree_html  =etree.HTML(result)
    data = etree_html.xpath("//td[contains(@title,'必发')]/../td[3]//@klfc")
    data = '      '.join(data)
    return data

# Matchbook离散值
def exchange_Matchbook(temp):
    url = f'https://odds.500.com/fenxi/ouzhi-{temp["fid"]}.shtml?ctype=3'
    while True:
        number = 1
        try:
            response = requests.get(url, headers=headers)
            break
        except:
            time.sleep(1)
            print('第{}次获取Matchbook失败'.format(number))
            number += 1
    response.encoding = 'GBK'
    result = response.text
    etree_html = etree.HTML(result)
    data = etree_html.xpath('//*[@id="142"]/td[3]/table/tbody/tr/td/@klfc')
    data = '      '.join(data)
    return data

# 获取Leon离散值
def exchange_leon(temp):
    url = f'https://odds.500.com/fenxi/ouzhi-{temp["fid"]}.shtml?ctype=3'
    while True:
        number = 1
        try:
            response = requests.get(url,headers=headers)
            break
        except:
            time.sleep(1)
            print('第{}次获取leon数据失败'.format(number))
    response.encoding = 'GBK'
    result = response.text
    etree_html = etree.HTML(result)
    data = etree_html.xpath('//*[@id="1001"]/td[3]/table/tbody/tr/td/@klfc')
    data = '     '.join(data)
    return data

# 获取主流公司离散值
def main_compaines(temp):
    url = f'https://odds.500.com/fenxi/ouzhi-{temp["fid"]}.shtml?ctype=2'
    while True:
        number = 1
        try:
            response = requests.get(url, headers=headers)
            break
        except:
            time.sleep(1)
            print('获取主流公司数据第{}次失败'.format(number))
    response.encoding = 'GBK'
    klfc1 = []
    klfc2 = []
    klfc3 = []
    klfc4 = []
    klfc5 = []
    klfc6 = []
    result = response.text
    etree_html = etree.HTML(result)
    tds = etree_html.xpath('//table[@id="datatb"]/tbody/tr')
    current_time_ticks = time.time()
    format = '%Y-%m-%d %H:%M:%S'
    for td in tds:
        update_times = td.xpath('//table[@id="datatb"]/tbody/tr/@data-time')
        for update_time in update_times:
            
            update_time_ticks = time.mktime(time.strptime(update_time, format)
            differ_time = current_time_ticks - update_time_ticks
            if int(differ_time) <= 3600*3:
                continue
            # //table[@id="datatb"]/tbody/tr//td[3]/table/tbody/tr/td/@klfc
            all_data = td.xpath('//*[@id="1"]/td[3]/table/tbody/tr/td/@klfc')
            klfc1.append(float(all_data[0]))
            klfc2.append(float(all_data[1]))
            klfc3.append(float(all_data[2]))
            klfc4.append(float(all_data[3]))
            klfc5.append(float(all_data[4]))
            klfc6.append(float(all_data[5]))
    data = [str(i) for i [
    round(sum(klfc1) / len(klfc1), 2),
    round(sum(klfc2) / len(klfc2), 2),
    round(sum(klfc3) / len(klfc3), 2),
    round(sum(klfc4) / len(klfc4), 2),
    round(sum(klfc5) / len(klfc5), 2),
    round(sum(klfc5) / len(klfc5), 2)]]
    return data





if __name__=='__main__':
    t1 = threading.Thread(target=parse_match_list)
    t1.start()
    # parse_match_list()

    # print(all_companies())
