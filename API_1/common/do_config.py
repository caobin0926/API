import configparser

class Config:
    def __init__(self,conf_filePath,encoding='utf-8'):
        self.cf=configparser.ConfigParser()
        self.cf.read(conf_filePath,encoding)
    def get_intValue(self,section,option):
        return self.cf.getint(section,option)
    def get_boolean(self,section,option):
        return self.cf.getboolean(section,option)
    def get_str(self,section,option):
        return self.cf.get(section,option)
    def get_float(self,section,option):
        return self.cf.getfloat(section,option)

from API_1.config import path
if __name__=='__main__':
    cf=Config(path.mysql_file)
    print(cf.get_str('test','host'))