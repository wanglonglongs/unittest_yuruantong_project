import yaml
from  yuruantong_pc.common.handle_path import config_path

def get_yaml_data(fileDir):
    #方法一
    # # 1、打开文件
    # fo = open(fileDir, 'r', encoding='utf-8')
    # # 2、读取文件
    # yaml_data = yaml.load(fo, Loader=yaml.FullLoader)
    # return yamldata
    #方法二
    with open(fileDir, encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())


if __name__ == '__main__':
    print(get_yaml_data(f'{config_path}\locator.yaml'))

