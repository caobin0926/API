import pymysql
from API_1.config import path
from API_1.common.do_config import Config

class Mysql:
    """封装操作mysql库的类"""
    def __init__(self):
        cf=Config(path.mysql_file)
        self.host=cf.get_str('test','host')
        self.port=cf.get_intValue('test','port')
        self.database=cf.get_str('test','database')
        self.user=cf.get_str('test','user')
        self.password=cf.get_str('test','password')
        self.sql=pymysql.connect(host=self.host,port=self.port,database=self.database,
                                 user=self.user,password=self.password,charset='utf8')
        self.cursor = self.sql.cursor(pymysql.cursors.DictCursor)
    def read_mysql(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def write_mysql_data(self,sql):
        self.cursor.execute(sql)
    def mysql_close(self):
        self.cursor.close()
        self.sql.close()

if __name__=='__main__':
    mysql=Mysql()
    a=mysql.read_mysql("select id from  future.member where mobilephone='18106573747'")
    mysql.mysql_close()
    print(a)





