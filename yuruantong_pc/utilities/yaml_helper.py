import yaml


class YamlHelper:
    # 定义一个静态方法read_yaml，它接收一个yaml文件路径参数
    @staticmethod
    def read_yaml(yaml_file_path):
        # 使用 with打开文件，‘r’表示只读模式，as 关键字将文件对象赋值给变量  stream
        with open(yaml_file_path, 'r') as stream:
            try:
                # 使用PyYAML中的safe_load 方法读取 yaml 文件内容，并返回结果
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)