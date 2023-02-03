import wol
import sys


def boot_computer(s):
    try:
        if s == '-h':
            print('参数使用方法：python3 main_boot_computer.py mac地址\npython3 main_boot_computer.py 98:90:96:C1:FE:CB')
        else:
            print('正在向 ', s, ' 发送魔法唤醒包！')
            mac = wol.format_mac(s)
            send_data = wol.create_magic_packet(mac)
            wol.send_magic_packet(send_data)
            return '成功向' + s + '发送唤醒包！'
    except ValueError:
        print('未收到传入的参数\n获取帮助：python3 main_boot_computer.py -h')


if __name__ == '__main__':
    # DSM
    DSM_mac = '00:26:2D:06:7C:A4'
    # ubuntu
    ub_mac = '00:E0:66:9E:FF:F7'
    # boot_computer(mac)
    # ESXi
    ESXi_mac = '60:45:CB:73:E3:D5'

    print('1:DSM\r\n'
          '2:ubuntu\r\n'
          '3:ESXi\r\n')
    slt_num = input('请输入选择要唤醒设备的序号：')
    if slt_num == "1":
        boot_computer(DSM_mac)
    elif slt_num == '2':
        boot_computer(ub_mac)
    elif slt_num == '3':
        boot_computer(ESXi_mac)
    else:
        print('请输入正确的数字！')

