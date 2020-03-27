import random
from faker import Faker


def phone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


# 随机生成姓名和身份证号
class UserBase:
    def __init__(self):
        fake = Faker('zh_CN')
        dicts = {}
        for _ in range(10):
            dict1 = fake.simple_profile(sex=None)
            self.name = dict1.get('name')
            self.cardid = fake.ssn()
            dicts[self.name] = self.cardid



class TestData:
    register_cell=phone()
    register_pwd='123456'



import re
def replace(data):
    data_new=data
    p='%(.*?)%'
    while re.search(p,data_new):
        result=re.search(p,data_new)
        g=result.group(1)
        if getattr(TestData,g):
            data_new=re.sub(p,str(getattr(TestData,g)),data_new,count=1)
    return data_new
if __name__=='__main__':
    data= "{'mobilephone':'%register_cell%','pwd':'%register_pwd%'}"
    print(replace(data))
    # print(TestData.register_cell)



