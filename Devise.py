from Based import *
from Protocol import UDP

class PC(Node):
    def __init__(self, Status="off", ip='1' , Mac='a', port='notc', con=None):
        super().__init__(Status,Mac, con, port)
        self.__ip=ip

    def Receve(self, Pocet):
        tmp=UDP()
        tmp.dectruct(Pocet)
        if tmp.chek_hex(tmp.ethernet_header(), tmp.ip_header(), tmp.udp_header(),tmp.get_type) == 5:
            print(tmp.get_date)
            self.bed_pocet(tmp.get_send)

        else:
            if tmp.get_res == self.get_ip:
                if tmp.get_date[0]==1:
                    print("Data: ", tmp.get_date[1])
                    print('ping complete', 'sourse', self.get_ip, 'sender', tmp.get_send)
                    self.res_ping(tmp.get_send, 17)
                elif tmp.get_date[0]==2:
                    print(tmp.get_date[1])
                    print('ping complete', 'sourse',self.get_ip, 'sender', tmp.get_send)
                
            else:
                pass
                #print(f'eror wrong ip {tmp.get_res, self.get_ip}')
                #print(self.get_ip)

    def Transmit(self, poket):
        print(
            f"[{self.get_mac}] Відправляю пакет через {self.get_con.get_mac if self.get_con else 'немає підключення'}")
        if self.get_con:
            self.get_con.Receve(poket)
        else:
            print(f"[{self.get_mac}] Немає підключення!")




    @property
    def get_ip(self):
        return self.__ip

    def set_ip(self, tmp):
        self.__ip = tmp

    def newpacket(self, res, data, type):
        udp_instance = UDP(type, self.get_ip, res, data, '', 20, 20,)  # Створюємо об'єкт UDP
        return udp_instance.Сollect_Poket()

    def ping(self, vere, type):
        for i in range(4):
            self.Transmit(self.newpacket(vere,[1,f'{i} ping', 3],type))

    def res_ping(self, vere, type):
        self.Transmit(self.newpacket(vere, [2,f'resive ping',3],type))

    def bed_pocet(self, vere, type=18):
        self.Transmit(self.newpacket(vere, [3, 'bed poctek', 3], type))


class Swish(Node):
    def __init__(self, Status="off", Mac='a', potr={}, dev_mac={}):
        super().__init__(Status, Mac, potr)
        self.__row_table = {}
        self.__dev_mac = dev_mac

    @property
    def get_devm(self):
        return self.__dev_mac



    @property
    def get_tabl(self):
        return self.__row_table

    def set_tabl(self, tmp):
        self.__row_table = tmp

    def update_mac_table(self, mac_address, device):
        self.get_tabl[mac_address] = device  # переконайтеся, що device передається вірно
        print(f"[{self.get_mac}] Оновлено MAC-Таблицю: {self.__row_table}")

    def Receve(self, Pocet):
        tmp = UDP()
        tmp.dectruct(Pocet)

        src_mac = tmp.get_smac
        dst_mac = tmp.get_dmac

        # TTL контроль
        if tmp.get_date[2] <= 0:
            print(f"[{self.get_mac}] TTL вичерпано. Пакет відкидається.")
            return

        tmp.get_date[2] -= 1  # Зменшуємо TTL

        # Оновлюємо MAC-таблицю, але тільки якщо пристрій підтримує її
        if src_mac not in self.get_tabl :
            self.update_mac_table(src_mac, self.get_devm.get(src_mac))

        # Якщо знаємо MAC-адресу одержувача – передаємо напряму
        if dst_mac in self.get_tabl:
            print(f"[{self.get_mac}] Знайдено отримувача {dst_mac}, передаю без розсилки.")
            self.get_tabl[dst_mac].Receve(tmp.Сollect_Poket())
        else:
            # Якщо не знаємо MAC, передаємо всім, але перевіряємо чи не PC
            print(f"[{self.get_mac}] MAC {dst_mac} невідомий, відправляю всім.")
            for device in self.get_port.values():
                if device.get_mac != src_mac:  # Не відправляємо назад
                    if hasattr(device, "Receve"):  # Перевіряємо, чи може прийняти
                        device.Receve(tmp.Сollect_Poket())



class Route(Node):

    def __init__(self, Status="off", Mac='a', potr={}):
        super().__init__(Status, Mac, potr)
