import re
import time
from flask import Flask, jsonify, request
from find_data import find_GamesData, find_GamesData_spider, find_loginuser, find_immediateData, find_front30Data, \
    find_front1Data, find_front3Data, find_front5Data, find_endData
from flask_cors import CORS
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from spider import get_match_data, manual_spider

app = Flask(__name__)
app.config['ENV']='development'

CORS(app, supports_credentials=True)
scheduler = APScheduler()
scheduler.init_app(app=app)
scheduler = BackgroundScheduler(timezone="Asia/Shanghai")

# 查询数据
@app.route('/find_data')
def find_data():
    url=request.url
    res = re.match('http.*?value.*?=(.*?)T.*?value.*?=(.*?)T', url)
    if res!=None:
        Start_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(1), "%Y-%m-%d")))+86400))[5:]+' 00:00'
        End_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(2), "%Y-%m-%d")))+86400))[5:]+' 23:59'
        mytime=[Start_date,End_date]
        myGamesData=find_GamesData(mytime)
    else:
        mytime=[]
        myGamesData=find_GamesData(mytime)
    return jsonify({'data': myGamesData}, {'meta':[{'msg':'查询成功'},{'statu':'200'}]})

# 查询即时比赛数据
@app.route('/find_immediateData')
def find_immediate():
    url=request.url
    res = re.match('http.*?value.*?=(.*?)T.*?value.*?=(.*?)T', url)
    if res!=None:
        Start_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(1), "%Y-%m-%d")))+86400))[5:]+' 00:00'
        End_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(2), "%Y-%m-%d")))+86400))[5:]+' 23:59'
        mytime=[Start_date,End_date]
        myGamesData=find_immediateData(mytime)
    else:
        mytime=[]
        myGamesData=find_immediateData(mytime)
    return jsonify({'data': myGamesData}, {'meta':[{'msg':'查询成功'},{'statu':'200'}]})


# 查询比赛前30分钟的数据
@app.route('/find_front30Data')
def find_front30():
    url=request.url
    res = re.match('http.*?value.*?=(.*?)T.*?value.*?=(.*?)T', url)
    if res!=None:
        Start_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(1), "%Y-%m-%d")))+86400))[5:]+' 00:00'
        End_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(2), "%Y-%m-%d")))+86400))[5:]+' 23:59'
        mytime=[Start_date,End_date]
        myGamesData=find_front30Data(mytime)
    else:
        mytime=[]
        myGamesData=find_front30Data(mytime)
    return jsonify({'data': myGamesData}, {'meta':[{'msg':'查询成功'},{'statu':'200'}]})

# 查询比赛前1小时的数据
@app.route('/find_front1Data')
def find_front1():
    url=request.url
    res = re.match('http.*?value.*?=(.*?)T.*?value.*?=(.*?)T', url)
    if res!=None:
        Start_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(1), "%Y-%m-%d")))+86400))[5:]+' 00:00'
        End_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(2), "%Y-%m-%d")))+86400))[5:]+' 23:59'
        mytime=[Start_date,End_date]
        myGamesData=find_front1Data(mytime)
    else:
        mytime=[]
        myGamesData=find_front1Data(mytime)
    return jsonify({'data': myGamesData}, {'meta':[{'msg':'查询成功'},{'statu':'200'}]})

# 查询比赛前3小时的数据
@app.route('/find_front3Data')
def find_front3():
    url=request.url
    res = re.match('http.*?value.*?=(.*?)T.*?value.*?=(.*?)T', url)
    if res!=None:
        Start_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(1), "%Y-%m-%d")))+86400))[5:]+' 00:00'
        End_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(2), "%Y-%m-%d")))+86400))[5:]+' 23:59'
        mytime=[Start_date,End_date]
        myGamesData=find_front3Data(mytime)
    else:
        mytime=[]
        myGamesData=find_front3Data(mytime)
    return jsonify({'data': myGamesData}, {'meta':[{'msg':'查询成功'},{'statu':'200'}]})

# 查询比赛前5小时的数据
@app.route('/find_front5Data')
def find_front5():
    url=request.url
    res = re.match('http.*?value.*?=(.*?)T.*?value.*?=(.*?)T', url)
    if res!=None:
        Start_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(1), "%Y-%m-%d")))+86400))[5:]+' 00:00'
        End_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(2), "%Y-%m-%d")))+86400))[5:]+' 23:59'
        mytime=[Start_date,End_date]
        print(mytime)
        myGamesData=find_front5Data(mytime)
    else:
        mytime=[]
        myGamesData=find_front5Data(mytime)
    return jsonify({'data': myGamesData}, {'meta':[{'msg':'查询成功'},{'statu':'200'}]})

# 查询比赛结束的数据
@app.route('/find_endData')
def find_end():
    url=request.url
    res = re.match('http.*?value.*?=(.*?)T.*?value.*?=(.*?)T', url)
    if res!=None:
        Start_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(1), "%Y-%m-%d")))+86400))[5:]+' 00:00'
        End_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(2), "%Y-%m-%d")))+86400))[5:]+' 23:59'
        mytime=[Start_date,End_date]
        myGamesData=find_endData(mytime)
    else:
        mytime=[]
        myGamesData=find_endData(mytime)
    return jsonify({'data': myGamesData}, {'meta':[{'msg':'查询成功'},{'statu':'200'}]})

# 查询手动启动爬虫数据
@app.route('/find_spider_data')
def find_spider_data():
    url=request.url
    res = re.match('http.*?value.*?=(.*?)T.*?value.*?=(.*?)T', url)
    if res!=None:
        Start_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(1), "%Y-%m-%d")))+86400))[5:]+' 00:00'
        End_date=time.strftime("%Y-%m-%d",time.localtime(int(time.mktime(time.strptime(res.group(2), "%Y-%m-%d")))+86400))[5:]+' 23:59'
        mytime=[Start_date,End_date]
        myGamesData=find_GamesData_spider(mytime)
    else:
        mytime=[]
        myGamesData=find_GamesData_spider(mytime)
    return jsonify({'data': myGamesData}, {'meta':[{'msg':'查询成功'},{'statu':'200'}]})

# 启动爬虫
@app.route('/startspider')
def startSipder():
    manual_spider()
    return jsonify({'data': '启动成功'}, {'meta':[{'msg':'启动成功'},{'statu':'200'}]})

# 登录
@app.route('/login')
def login():
    name = request.args.get('username')
    password = request.args.get('password')
    mylist=find_loginuser(name, password)
    return jsonify({'data':{'token':mylist[0]}},{'meta':[{'msg':mylist[2]},{'statu':mylist[1]}]})

# scheduler.add_job(func=get_match_data, id='1', trigger='cron', minute ='00,05,10,15,20,25,30,35,40,45,50,55')
# scheduler.start()
if __name__ == '__main__':
    app.run(debug=False,port=9000, host='0.0.0.0')
