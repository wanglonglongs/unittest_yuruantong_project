import os
from configparser import ConfigParser
from yuruantong_pc.common.save_package.getfiledir import CONFDIR


class Config(ConfigParser):

    def __init__(self):
        self.conf_name = os.path.join(CONFDIR, 'base.ini')
        super().__init__()
        super().read(self.conf_name, encoding='utf-8')


    def save_data(self, section, option, value):
        super().set(section=section, option=option, value=value)
        super().write(fp=open(self.conf_name, 'w'))

# con = Config()
# type = con.get('base', 'browser_type')
# print(type)


