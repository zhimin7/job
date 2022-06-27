import pymysql

host = '175.178.14.211'
user = 'lottery_500_2'
passwd = '698350As?'
port = 3306
mydb = 'lottery_500_2'

################################保存即时比赛数据################################
# 创建数据库
def create_db_now():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port)
    cursor = db.cursor()
    sql = f'create database if not exists {mydb} default character set utf8'
    cursor.execute(sql)
    db.close()
    create_table_now()

# 创建数据表
def create_table_now():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'create table if not exists now_data_now (fid varchar(255) not null, gamestime varchar(255) not null,delayed_time varchar(255) not null,spider_time varchar(255) null,home_team varchar(255) not null,score varchar(255) not null,away_team varchar(255) not null,handicap varchar(255) not null,All_companies varchar(255) not null,BiFa varchar(255) not null,Matchbook varchar(255) not null,Leon varchar(255) not null,Betsson varchar(255) not null,mainstream_companines_3 varchar(255) not null,mainstream_companines_1 varchar(255) not null,Exchange varchar(255) not null)'
    cursor.execute(sql)
    db.close()

# 保存比赛即时的数据表
def saving_table_now(srr):
    create_db_now()
    db = pymysql.connect(host=host, user=user, password=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'insert into now_data_now (fid, gamestime,delayed_time, spider_time,home_team,score,away_team,handicap,All_companies, BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, list(srr.values()))
        print(list(srr.values()))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
###############################################################################

################################保存比赛前30分钟数据################################
# 创建数据库
def create_db_now30():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port)
    cursor = db.cursor()
    sql = f'create database if not exists {mydb} default character set utf8'
    cursor.execute(sql)
    db.close()
    create_table_now30()

# 创建数据表
def create_table_now30():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'create table if not exists now_data_now30 (fid varchar(255) not null, gamestime varchar(255) not null,delayed_time varchar(255) not null,spider_time varchar(255) null,home_team varchar(255) not null,score varchar(255) not null,away_team varchar(255) not null,handicap varchar(255) not null,All_companies varchar(255) not null,BiFa varchar(255) not null,Matchbook varchar(255) not null,Leon varchar(255) not null,Betsson varchar(255) not null,mainstream_companines_3 varchar(255) not null,mainstream_companines_1 varchar(255) not null,Exchange varchar(255) not null)'
    cursor.execute(sql)
    db.close()

# 保存比赛即时的数据表
def saving_table_now30(srr):
    create_db_now30()
    db = pymysql.connect(host=host, user=user, password=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'insert into now_data_now30 (fid, gamestime,delayed_time, spider_time,home_team,score,away_team,handicap,All_companies, BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, list(srr.values()))
        print(list(srr.values()))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
###############################################################################

################################保存比赛前1小时数据################################
# 创建数据库
def create_db_now1():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port)
    cursor = db.cursor()
    sql = f'create database if not exists {mydb} default character set utf8'
    cursor.execute(sql)
    db.close()
    create_table_now1()

# 创建数据表
def create_table_now1():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'create table if not exists now_data_now1 (fid varchar(255) not null, gamestime varchar(255) not null,delayed_time varchar(255) not null,spider_time varchar(255) null,home_team varchar(255) not null,score varchar(255) not null,away_team varchar(255) not null,handicap varchar(255) not null,All_companies varchar(255) not null,BiFa varchar(255) not null,Matchbook varchar(255) not null,Leon varchar(255) not null,Betsson varchar(255) not null,mainstream_companines_3 varchar(255) not null,mainstream_companines_1 varchar(255) not null,Exchange varchar(255) not null)'
    cursor.execute(sql)
    db.close()

# 保存比赛前1小时数据
def saving_table_now1(srr):
    create_db_now1()
    db = pymysql.connect(host=host, user=user, password=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'insert into now_data_now1 (fid, gamestime,delayed_time, spider_time,home_team,score,away_team,handicap,All_companies, BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, list(srr.values()))
        print(list(srr.values()))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
###############################################################################

################################保存比赛前3小时数据################################
# 创建数据库
def create_db_now3():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port)
    cursor = db.cursor()
    sql = f'create database if not exists {mydb} default character set utf8'
    cursor.execute(sql)
    db.close()
    create_table_now3()

# 创建数据表
def create_table_now3():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'create table if not exists now_data_now3 (fid varchar(255) not null, gamestime varchar(255) not null,delayed_time varchar(255) not null,spider_time varchar(255) null,home_team varchar(255) not null,score varchar(255) not null,away_team varchar(255) not null,handicap varchar(255) not null,All_companies varchar(255) not null,BiFa varchar(255) not null,Matchbook varchar(255) not null,Leon varchar(255) not null,Betsson varchar(255) not null,mainstream_companines_3 varchar(255) not null,mainstream_companines_1 varchar(255) not null,Exchange varchar(255) not null)'
    cursor.execute(sql)
    db.close()

# 保存比赛前3小时数据
def saving_table_now3(srr):
    create_db_now3()
    db = pymysql.connect(host=host, user=user, password=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'insert into now_data_now3 (fid, gamestime,delayed_time, spider_time,home_team,score,away_team,handicap,All_companies, BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, list(srr.values()))
        print(list(srr.values()))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
###############################################################################


################################保存比赛前5小时数据################################
# 创建数据库
def create_db_now5():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port)
    cursor = db.cursor()
    sql = f'create database if not exists {mydb} default character set utf8'
    cursor.execute(sql)
    db.close()
    create_table_now5()

# 创建数据表
def create_table_now5():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'create table if not exists now_data_now5 (fid varchar(255) not null, gamestime varchar(255) not null,delayed_time varchar(255) not null,spider_time varchar(255) null,home_team varchar(255) not null,score varchar(255) not null,away_team varchar(255) not null,handicap varchar(255) not null,All_companies varchar(255) not null,BiFa varchar(255) not null,Matchbook varchar(255) not null,Leon varchar(255) not null,Betsson varchar(255) not null,mainstream_companines_3 varchar(255) not null,mainstream_companines_1 varchar(255) not null,Exchange varchar(255) not null)'
    cursor.execute(sql)
    db.close()

# 保存比赛前5小时数据
def saving_table_now5(srr):
    create_db_now5()
    db = pymysql.connect(host=host, user=user, password=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'insert into now_data_now5 (fid, gamestime,delayed_time, spider_time,home_team,score,away_team,handicap,All_companies, BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, list(srr.values()))
        print(list(srr.values()))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
###############################################################################


##########################################手动启动爬虫数据##########################
# 创建数据库
def create_db_start():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port)
    cursor = db.cursor()
    sql = f'create database if not exists {mydb} default character set utf8'
    cursor.execute(sql)
    db.close()
    create_table_start()

# 创建数据表
def create_table_start():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'create table if not exists now_data_start (fid varchar(255) not null, gamestime varchar(255) not null,delayed_time varchar(255) not null,spider_time varchar(255) null,home_team varchar(255) not null,score varchar(255) not null,away_team varchar(255) not null,handicap varchar(255) not null,All_companies varchar(255) not null,BiFa varchar(255) not null,Matchbook varchar(255) not null,Leon varchar(255) not null,Betsson varchar(255) not null,mainstream_companines_3 varchar(255) not null,mainstream_companines_1 varchar(255) not null,Exchange varchar(255) not null)'
    cursor.execute(sql)
    db.close()

# 保存手动启动爬虫数据
def saving_table_start(srr):
    create_db_start()
    db = pymysql.connect(host=host, user=user, password=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'insert into now_data_start (fid, gamestime,delayed_time, spider_time,home_team,score,away_team,handicap,All_companies, BiFa,Matchbook,Leon,Betsson,mainstream_companines_3,mainstream_companines_1,Exchange) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, list(srr.values()))
        print(list(srr.values()))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()
##############################################################################


#####################################创建用户数据################################
# 创建数据库
def create_db_user():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port)
    cursor = db.cursor()
    sql = f'create database if not exists {mydb} default character set utf8'
    cursor.execute(sql)
    db.close()
    create_table_user()

# 创建数据表
def create_table_user():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'create table if not exists usertable (uid varchar(10) not null ,username varchar(50)  not null ,password varchar(30)  not null)'
    cursor.execute(sql)
    db.close()
##############################################################################

#######################################保存比赛结束的数据信息####################
# 创建数据库
def create_db_end():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port)
    cursor = db.cursor()
    sql = f'create database if not exists {mydb} default character set utf8'
    cursor.execute(sql)
    db.close()
    create_table_end()

# 创建数据表
def create_table_end():
    db = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'create table if not exists now_data_end (fid varchar(255) not null primary key, gamestime varchar(255) not null,home_team varchar(255) not null,score varchar(255) not null,away_team varchar(255) not null)'
    cursor.execute(sql)
    db.close()

# 保存比赛结束数据
def saving_table_end(srr):
    create_db_end()
    db = pymysql.connect(host=host, user=user, password=passwd, port=port, db=mydb)
    cursor = db.cursor()
    sql = 'insert into now_data_end (fid, gamestime,home_team,score,away_team) values(%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, list(srr.values()))
        print(list(srr.values()))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()

#########################################################################

def delete_data_now_start():
    db=pymysql.connect(host=host,user=user,passwd=passwd,port=port,db=mydb)
    cursor=db.cursor()
    sql='DELETE FROM now_data_start'
    cursor.execute(sql)
    db.commit()
    db.close()