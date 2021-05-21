                   #By priyansh bakhtani

import mysql.connector as con
db=con.connect(host='localhost',user='root',passwd='root',database='liveChat')
print(db)
cu=db.cursor()

# sql="create database liveChat"
# cu.execute(sql)

# cu.execute("show databases")
# for x in cu:
#     print(x)

def createtable():
    sql='create table user ' \
        '(uid int primary key auto_increment,email varchar(45),password varchar(25),firstname varchar(25),' \
        'lastname varchar(25),prnNo int)'
    cu.execute(sql)
# createtable()
def showtable():
    sql='show tables'
    cu.execute(sql)
    for x in cu:
        print(x)
showtable()
def selectuser():
    sql='select * from user'
    cu.execute(sql)
    res=cu.fetchall()
    print(res)
selectuser()