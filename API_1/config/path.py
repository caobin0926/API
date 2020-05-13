import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#测试库配置文件地址
mysql_file=os.path.join(base_dir,'config','mysql.cfg')
# print(mysql_file)
environment_file=os.path.join(base_dir,'config','environment.cfg')

logs_file=os.path.join(base_dir,'log','py15.txt')
# print(logs_file)
logs_cfg=os.path.join(base_dir,'config','log.cfg')
# print(logs_cfg)
case_file=os.path.join(base_dir,'data','cases.xlsx')
#登录测试用例路径
login_yml=os.path.join(base_dir,'data','login.yaml')
#注册测试用例路径
register_yml=os.path.join(base_dir,'data','register.yml')


