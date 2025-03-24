

class Node:
    def __init__(self, Status="off", Mac=0, con='zero', port='notc'):
        self.__Status = Status
        self.__Mac=Mac
        self.__con = con
        self.__port = port

    @property
    def get_st(self):
        return self.__Status

    def set_st(self, st):
        self.__Status = st

    @property
    def get_port(self):
        return self.__port

    def set_port(self, tmp):
        self.__port = tmp

    @property
    def get_mac(self):
        return self.__Mac

    def set_mac(self, tmp):
        self.__Mac = tmp

    @property
    def get_con(self):
        return self.__con

    def set_con(self, tmp):
        self.__con = tmp

    def on_off(self):
        if self.get_st == "off":
            self.set_st ="on"
        else:
            self.set_st ="off"

    def Receve(self, Pocet):
        pass

    def Transmit(self, poket):
        pass

    def conect(self):
        pass

class Poket:
    def __init__(self, Type="empty",Sender="empty", Receiver="empty", Date='empty', Checksum='empty', Sourse_Port='empty',Destination_Port='empty',leng='empty', src_mac="00", dst_mac="FF:", arp_table=1):
        self.__Type = Type
        self.__Sender = Sender
        self.__Receiver = Receiver
        self.__Date = Date
        self.__Checksum = Checksum
        self.__Sourse_Port = Sourse_Port
        self.__Destination_Port = Destination_Port
        self.__leng =leng
        self.__src_mac = src_mac
        self.__dst_mac = dst_mac
        self.__arp = arp_table

    def v4tobit(self, ip):
        parts = ip.split('.')
        return ''.join(format(int(part), '08b') for part in parts)

    def bittov4(self, bit):
        return ".".join(str(int(bit[i:i + 8], 2)) for i in range(0, 32, 8))

    def bit_to_normal(self, bit):
        return [int(bits, 2) for bits in bit]

    def mac_to_bin(self, mac):
        return ''.join(format(int(x, 16), '08b') for x in mac.split(':'))

    def bin_to_mac(self, bin_mac):
        return ':'.join(format(int(bin_mac[i:i + 8], 2), '02x') for i in range(0, 48, 8))




    @property
    def get_type(self):
        return self.__Type

    def set_type(self, tmp):
        self.__Type = tmp

    @property
    def get_send(self):
        return self.__Sender

    def set_send(self, tmp):
        self.__Sender = tmp

    @property
    def get_res(self):
        return self.__Receiver

    def set_res(self, tmp):
        self.__Receiver = tmp


    @property
    def get_date(self):
        return self.__Date

    def set_date(self, tmp):
        self.__Date = tmp

    @property
    def get_sum(self):
        return self.__Checksum

    def set_sum(self, tmp):
        self.__Checksum = tmp

    @property
    def get_cp(self):
        return self.__Sourse_Port

    def set_cp(self, tmp):
        self.__Sourse_Port = tmp

    @property
    def get_dp(self):
        return self.__Destination_Port

    def set_dp(self, tmp):
        self.__Destination_Port = tmp

    @property
    def get_leng(self):
        return self.__leng

    def set_leng(self, tmp):
        self.__leng = tmp

    @property
    def get_smac(self):
        return self.__src_mac

    def set_smac(self, tmp):
        self.__src_mac = tmp

    @property
    def get_dmac(self):
        return self.__dst_mac

    def set_dmac(self, tmp):
        self.__dst_mac = tmp

    @property
    def get_arp(self):
        return self.__arp

    def set_arp(self, tmp):
        self.__arp = tmp

    def chek_hex(self,e_h, ip_h, udp_h, type):
        tmp=ip_h[len(ip_h)-1]
        ip_h.pop()
        self.set_sum(format(hash(tuple(e_h + ip_h + udp_h)) & 0xFFFF, '016b'))
        if (tmp == self.get_sum):
            return 1
        else:
            if type == 17:
             print('gg pocket fold')
            else:
                return 5