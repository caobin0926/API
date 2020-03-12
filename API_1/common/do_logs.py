import logging
from API_1.config import path
from API_1.common import do_config
class Logs:
    def __init__(self,logsName):
        #创建收集器
        self.logger=logging.getLogger(logsName)
        # #设置收集日志的级别
        self.logger.setLevel(level='DEBUG')
        #创建和设置输出渠道
        cf = do_config.Config(path.logs_cfg)
        file_handler=logging.FileHandler(path.logs_file,mode='a',encoding='utf-8') #文件渠道
        file_handler.setLevel(cf.get_str('logs','level'))#输出日志级别
        file_handler.setFormatter(logging.Formatter(cf.get_str('logs','fmt')))

        stream_handler=logging.StreamHandler()#控制台渠道
        stream_handler.setLevel(cf.get_str('logs','level'))#输出日志级别
        stream_handler.setFormatter(logging.Formatter(cf.get_str('logs','fmt')))
        #建立收集器和输出的关联关系
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def loggers(self,level,message):
        #DEBUG,INFO,WARNING,ERROR,CRITICAL
        if level.upper()=='DEBUG':
            self.logger.debug(message)
        elif level.upper()=='INFO':
            self.logger.info(message)
        elif level.upper()=='WARNING':
            self.logger.warning(message)
        elif level.upper()=='ERROR':
            self.logger.error(message)
        else:
            self.logger.critical(message)




if __name__=='__main__':
    logger=Logs('logss')
    logger.loggers('debug','测试debug')
    logger.loggers('info', '测试info')







