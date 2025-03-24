import math
import random


from based import Poket

class ARP:
    def __init__(self):
        self.arp_table = {
            '192.168.1.1': '00:11:22:33:44:55',  # MAC для PC1
            '192.168.1.2': '00:A1:B2:33:44:55',  # MAC для PC2
            '192.168.1.3': '00:BB:CC:DD:EE:FF',  # MAC для PC3
            '192.168.1.4': '00:11:22:33:44:66',  # MAC для PC4
            '192.168.1.5': '00:11:22:33:44:77'  # MAC для PC5
        }
    def get_mac_from_ip(self, ip_address):

        if ip_address in self.arp_table:
            return self.arp_table[ip_address]
        else:
            return None



class UDP(Poket):
    def __init__(self, Type="0",Sender=0, Receiver="0", Date="0", Checksum="0", Sourse_Port='0',Destination_Port='0', UDP_length=0,leng="empty",src_mac="00", dst_mac="FF:", arp_table=None):
        if arp_table is None:
            arp_table = ARP()
        super().__init__(Type,Sender, Receiver, Date, Checksum, Sourse_Port, Destination_Port, leng, src_mac, dst_mac, arp_table)
        self.__UDP_length=UDP_length

    def get_mac_from_ip(self, ip_address):

        mac_address = self.get_arp.get_mac_from_ip(ip_address)
        return mac_address

    @property
    def get_uleng(self):
        return self.__UDP_length

    def set_uleng(self, tmp):
        self.__UDP_length= tmp

    def ethernet_header(self):
        eth_header = []
        self.set_dmac(self.get_mac_from_ip(self.get_res))
        self.set_smac(self.get_mac_from_ip(self.get_send))
        eth_header.append(self.mac_to_bin(self.get_dmac))  # MAC-адреса отримувача
        eth_header.append(self.mac_to_bin(self.get_smac))  # MAC-адреса відправника
        return eth_header

    def udp_header(self):
        udp_header = []
        udp_header.append(self.v4tobit(self.get_send)) # sourse adres
        udp_header.append(self.v4tobit(self.get_res)) # адреса отримувача
        udp_header.append(format(0,'08b'))
        udp_header.append(format(self.get_type, '08b')) # протокол
        tmp=len(udp_header)
        udp_header.append(format(tmp, '016b')) #довжина udp
        return udp_header

    def ip_header(self):
        ip_header=[]

        ip_header.append(format(self.get_cp,'016b')) # Порт відправника
        ip_header.append(format(self.get_dp, '016b')) # Порт отримувача

        self.set_leng( 8 + math.ceil(len(self.get_date) / 8))
        ip_header.append(format(self.get_leng,'016b')) #довжина

        if random.randint(1,10) == 1:
            #ip_header.append(format(hash(tuple(self.ethernet_header() + ip_header + self.udp_header() +[1,2,3])) & 0xFFFF, '016b'))
            ip_header.append(format(hash(tuple(self.ethernet_header() + ip_header + self.udp_header())) & 0xFFFF, '016b'))
        else:
            #ip_header.append(format(hash(tuple(self.ethernet_header() + ip_header + self.udp_header())) & 0xFFFF, '016b'))
            ip_header.append(format(hash(tuple(self.ethernet_header() + ip_header + self.udp_header() + [1, 2, 3])) & 0xFFFF,'016b'))


        #print(f'{self.get_cp}    , {self.get_dp},  {self.get_leng}')

        return ip_header









    def Сollect_Poket(self):
        paket=[]
        paket.append(self.ethernet_header())
        paket.append(self.ip_header())
        paket.append(self.udp_header())
        paket.append(self.get_date)
        #print(paket)
        return paket




    def dectruct(self, poket):
        ethernet_header=[]
        ip_headers=[]
        udp_headers=[]
        self.set_date(poket[len(poket)-1])
        #print(self.get_date)
        poket.pop()
        udp_headers=poket[len(poket)-1]
        #print(udp_headers)
        poket.pop()
        ip_headers = poket[len(poket) - 1]
        #print(ip_headers)
        poket.pop()

        ethernet_header = poket[len(poket) - 1]
        # print(ethernet_header)
        poket.pop()



            # ----------------------ethernet------------------------------------
        self.set_smac(self.bin_to_mac(ethernet_header[len(ethernet_header)-1]))
        ethernet_header.pop()
        #print(self.get_smac)

        self.set_dmac(self.bin_to_mac(ethernet_header[len(ethernet_header) - 1]))
        ethernet_header.pop()
        #print(self.get_dmac)

                #----------------------ip------------------------------------

        self.set_dp(int(ip_headers[len(ip_headers) - 1], 2))  # порт отримувача
        ip_headers.pop()
        #print(self.get_dp)

        self.set_cp(int(ip_headers[len(ip_headers) - 1], 2))  # порт відправника
        ip_headers.pop()
        #print(self.get_cp)

        self.set_leng(int(ip_headers[len(ip_headers) - 1], 2))  # довжина
        ip_headers.pop()
        #print(self.get_leng)

        #---------------------------udp----------------------------

        self.set_uleng(int(udp_headers[len(udp_headers) - 1], 2))  # довжина udp
        udp_headers.pop()
        #print(self.get_uleng)

        self.set_type(int(udp_headers[len(udp_headers) - 1], 2))  # протокол
        udp_headers.pop()
        #print(self.get_type)
        udp_headers.pop() #нулі

        self.set_res(self.bittov4(udp_headers[len(udp_headers) - 1]))  # адреса отримувача
        udp_headers.pop()
        #print(self.get_res)

        self.set_send(self.bittov4(udp_headers[len(udp_headers) - 1]))  # адреса відправника
        udp_headers.pop()
        #print(self.get_send)















