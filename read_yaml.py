import yaml


def get_yaml_data(yaml_file):
    # 打开yaml文件
    # print("***获取yaml文件数据***")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    print(file_data)
    # print("类型：", type(file_data))

    # 将字符串转化为字典或列表
    # print("***转化yaml数据为字典或列表***")
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    # print(data)
    # print("类型：", type(data))
    return data


if __name__ == '__main__':
    # current_path = os.path.abspath(".")
    # yaml_path = os.path.join(current_path, "config.yaml")
    yaml_path = "./config.yaml"
    yaml_data = get_yaml_data(yaml_path)
    # print(yaml_data)
    lst_key = []
    lst_val = []
    # print(lst[i])
    for k, v in yaml_data.items():
        lst_key.append(k)
        lst_val.append(v)

    for i in range(len(lst_key)):
        print('数字{}为设备：{}'.format(i + 1, lst_key[i]))

    num = int(input('请输入数字:'))
    print('您选择的是设备MAC为：{}'.format(lst_val[num - 1]))
