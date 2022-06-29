import pymysql
import time
from datetime import datetime
host = '175.178.14.211'
user = 'lottery_500_2'
passwd = '698350As?'
port = 3306
mydb = 'lottery_500_2'
# 查询定时爬虫的数据
def find_GamesData(mytime):
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    if mytime==[]:
        now_times = (str(datetime.now())[:10])
        y_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) - 3600 * 24
        t_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) + 3600 * 24
        yesterday_time = time.strftime("%Y-%m-%d", time.localtime(y_time)) + ' 00:00:00'
        now_time = time.strftime("%Y-%m-%d", time.localtime(t_time)) + ' 23:59:59'
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from ((select * from now_data_now where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}") UNION ALL (select * from now_data_now30 where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}") UNION ALL (select * from now_data_now1 where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}") UNION ALL (select * from now_data_now3 where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}") UNION ALL (select * from now_data_now5 where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}"))n order by gamestime ,fid,delayed_time;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

    elif mytime!=[]:
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from ((select * from now_data_now) UNION ALL (select * from now_data_now30) UNION ALL (select * from now_data_now1) UNION ALL (select * from now_data_now3) UNION ALL (select * from now_data_now5) )n where  gamestime<="{mytime[1]}" and gamestime>="{mytime[0]}" order by gamestime ,fid,delayed_time;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist


# 查询手动启动爬虫数据
def find_GamesData_spider(mytime):
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    if mytime==[]:
        sql = 'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_start GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange order by gamestime ,fid,spider_time  ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

    elif mytime!=[]:
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_start where  gamestime<="{mytime[1]}" and gamestime>="{mytime[0]}" GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange  order by gamestime ,fid,spider_time;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

# 查询即时比赛的数据
def find_immediateData(mytime):
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    if mytime==[]:
        now_times = (str(datetime.now())[:10])
        y_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) - 3600 * 24
        t_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) + 3600 * 24
        yesterday_time = time.strftime("%Y-%m-%d", time.localtime(y_time)) + ' 00:00:00'
        now_time = time.strftime("%Y-%m-%d", time.localtime(t_time)) + ' 23:59:59'
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}"  GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange order by gamestime ,fid,spider_time  ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

    elif mytime!=[]:
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now where  gamestime<="{mytime[1]}" and gamestime>="{mytime[0]}" GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange  order by gamestime ,fid,spider_time;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

# 查询比赛前30分钟的数据
def find_front30Data(mytime):
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    if mytime==[]:
        now_times = (str(datetime.now())[:10])
        y_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) - 3600 * 24
        t_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) + 3600 * 24
        yesterday_time = time.strftime("%Y-%m-%d", time.localtime(y_time)) + ' 00:00:00'
        now_time = time.strftime("%Y-%m-%d", time.localtime(t_time)) + ' 23:59:59'
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now30 where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}"  GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange order by gamestime ,fid,spider_time  ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

    elif mytime!=[]:
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now30 where  gamestime<="{mytime[1]}" and gamestime>="{mytime[0]}" GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange  order by gamestime  ,fid,spider_time ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist


# 查询比赛前1小时的数据
def find_front1Data(mytime):
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    if mytime==[]:
        now_times = (str(datetime.now())[:10])
        y_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) - 3600 * 24
        t_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) + 3600 * 24
        yesterday_time = time.strftime("%Y-%m-%d", time.localtime(y_time)) + ' 00:00:00'
        now_time = time.strftime("%Y-%m-%d", time.localtime(t_time)) + ' 23:59:59'
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now1 where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}" GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange order by gamestime ,fid,spider_time  ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

    elif mytime!=[]:
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now1 where  gamestime<="{mytime[1]}" and gamestime>="{mytime[0]}" GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange  order by gamestime  ,fid,spider_time ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist


# 查询比赛前3小时的数据
def find_front3Data(mytime):
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    if mytime==[]:
        now_times = (str(datetime.now())[:10])
        y_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) - 3600 * 24
        t_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) + 3600 * 24
        yesterday_time = time.strftime("%Y-%m-%d", time.localtime(y_time)) + ' 00:00:00'
        now_time = time.strftime("%Y-%m-%d", time.localtime(t_time)) + ' 23:59:59'
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now3 where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}" GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange order by gamestime ,fid,spider_time  ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

    elif mytime!=[]:
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now3 where  gamestime<="{mytime[1]}" and gamestime>="{mytime[0]}" GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange  order by gamestime  ,fid,spider_time ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

# 查询比赛前5小时的数据
def find_front5Data(mytime):
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    if mytime==[]:
        now_times = (str(datetime.now())[:10])
        y_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) - 3600 * 24
        t_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) + 3600 * 24
        yesterday_time = time.strftime("%Y-%m-%d", time.localtime(y_time)) + ' 00:00:00'
        now_time = time.strftime("%Y-%m-%d", time.localtime(t_time)) + ' 23:59:59'
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now5 where gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}" GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange order by gamestime ,fid,spider_time  ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

    elif mytime!=[]:
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from now_data_now5 where  gamestime<="{mytime[1]}" and gamestime>="{mytime[0]}" GROUP BY fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange  order by gamestime  ,fid,spider_time ;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

# 查询比赛结束的数据
def find_endData(mytime):
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    if mytime==[]:
        now_times = (str(datetime.now())[:10])
        y_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) - 3600 * 24
        t_time = int(time.mktime(time.strptime(now_times, "%Y-%m-%d"))) + 3600 * 24
        yesterday_time = time.strftime("%Y-%m-%d", time.localtime(y_time)) + ' 00:00:00'
        now_time = time.strftime("%Y-%m-%d", time.localtime(t_time)) + ' 23:59:59'
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from ((select * from now_data_end where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}") UNION ALL (select * from now_data_now where  gamestime<="{now_time[5:16]}" and gamestime>="{yesterday_time[5:16]}"))n order by gamestime ,fid,delayed_time;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

    elif mytime!=[]:
        sql = f'select fid, gamestime,delayed_time,spider_time,home_team,score,away_team,handicap,All_companies,BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange from ((select * from now_data_now) UNION ALL (select * from now_data_end))n where  gamestime<="{mytime[1]}" and gamestime>="{mytime[0]}" order by gamestime ,fid,delayed_time;'
        cursor.execute(sql)
        res = cursor.fetchall()
        mylist=[]
        for i in res:
            mylist.append({'time':i[1],'spider_time':i[3],'home_team':i[4],'score':i[5],'away_team':i[6],'handicap':i[7],'All_companies':i[8],'BiFa':i[9],'Matchbook':i[10],'Leon':i[11],'Betsson':i[12],'mainstream_companines_3':i[13],'mainstream_companines_1':i[14],'Exchange':i[15]})
        return mylist

# 登录验证
def find_loginuser(username, password):
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = f'select * from usertable where  username="{username}" and password="{password}";'
    cursor.execute(sql)
    res = cursor.fetchall()
    if res != ():
        mylist = ['123', '200', '登录成功']
        return mylist
    elif res == ():
        mylist = ['', '404', '账号或密码错误']
        return mylist