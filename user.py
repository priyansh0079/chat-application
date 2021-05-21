                  #By priyansh bakhtani

import mysql.connector as con
db=con.connect(host='localhost',user='root',passwd='root',database='liveChat')
cu=db.cursor()

class User:
    def __init__(self):
        self.email=""
        self.password=""
        self.firstname=""
        self. lastname=""
        self.prn=""
    def createuser(self):
        sql='''insert into user    #user table in the database.
        (email,password,firstname,lastname,prnNo) 
        values
        (%s,%s,%s,%s,%s)'''
        value=(self.email,self.password,self.firstname,self.lastname,self.prn)
        cu.execute(sql,value)
        db.commit()
        rowcount=cu.rowcount
        return rowcount
    def validateUser(self):
        sql='select uid,email,firstname,lastname from user where email=%s and password=%s'
        value=(self.email,self.password)
        cu.execute(sql,value)
        res=cu.fetchone()
        return res




