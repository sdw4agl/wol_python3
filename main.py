from read_yaml import *
from send_mac import *
from ping_nums import *
import time

yaml_path = "/home/sdw4agl/wol/hm_config.yaml"
#yaml_path = "./18_config.yaml"
yaml_data = get_yaml_data(yaml_path)
lst_key = []
lst_val = []
#print(yaml_data)
for k, v in yaml_data.items():
    lst_key.append(k)
    lst_val.append(v)
#print(lst_key)
#print(lst_val)
len_key = len(lst_key)
print('设备数量为{}:'.format(len_key))
for i in range(len_key):
    print('{}#设备为：{}'.format(i + 1, lst_key[i]))

while True:
    input_char = input('请输入设备序号:')
    if input_char.isdigit():
        num = int(input_char)
        if num == 0:
            print('您输入的数字为0，请重新输入！')
        elif num - 1 < len_key:
            MAC_val = lst_val[num - 1]['MAC']
            IP_val = lst_val[num - 1]['IP_addr']
            slp_val = lst_val[num - 1]['slp_time']
            ping_val = lst_val[num - 1]['ping_num']
            print('您选择的是设备MAC为：{}'.format(MAC_val))
            print('您选择的是设备IP地址为：{}'.format(IP_val))
            print('您选择的是ping命令延时时间为：{}'.format(slp_val))
            print('您选择的是设备ping次数为：{}'.format(ping_val))
            # print('您选择的是设备MAC为：{}'.format(lst_val[num - 1]['MAC']))
            boot_computer(MAC_val)
            print('唤醒包已发送。')
            time.sleep(slp_val)
            ping(IP_val, ping_val)
            break
        else:
            print('您输入的数字大于设备数量，请重新输入！')
    else:
        print('您输入的字符不是数字，请重新输入！')
