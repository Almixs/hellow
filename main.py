from Devise import *


pc1 = PC('off', '192.168.1.1', '00:11:22:33:44:55'.lower(), 'e1')
pc2 = PC('off', '192.168.1.2', '00:A1:B2:33:44:55'.lower(), 'e1')
pc3 = PC('off', '192.168.1.3', '00:BB:CC:DD:EE:FF'.lower(), 'e1')
pc4 = PC('off', '192.168.1.4', '00:11:22:33:44:66'.lower(), 'e1')
pc5 = PC('off', '192.168.1.5', '00:11:22:33:44:77'.lower(), 'e1')

devise_mac = {
    '00:11:22:33:44:55'.lower(): pc1,
    '00:A1:B2:33:44:55'.lower(): pc2,
    '00:BB:CC:DD:EE:FF'.lower(): pc3,
    '00:11:22:33:44:66'.lower(): pc4,
    '00:11:22:33:44:77'.lower(): pc5
}

sw1 = Swish('off', 'FA:A1:B2:33:44:55'.lower(), 'e', devise_mac)
sw2 = Swish('off', 'FA:A1:B2:33:44:56'.lower(), 'e', devise_mac)
sw3 = Swish('off', 'FA:A1:B2:33:44:57'.lower(), 'e', devise_mac)
sw4 = Swish('off', 'FA:A1:B2:33:44:58'.lower(), 'e', devise_mac)
sw5 = Swish('off', 'FA:A1:B2:33:44:59'.lower(), 'e', devise_mac)

pc1.set_con(sw1)
pc2.set_con(sw2)
pc3.set_con(sw3)
pc4.set_con(sw4)
pc5.set_con(sw5)

sw1.set_port({'e1': pc1, 'e2': sw2, 'e3': sw5})
sw2.set_port({'e1': pc2, 'e2': sw1, 'e3': sw3})
sw3.set_port({'e1': pc3, 'e2': sw2, 'e3': sw4})
sw4.set_port({'e1': pc4, 'e2': sw3, 'e3': sw5})
sw5.set_port({'e1': pc5, 'e2': sw1, 'e3': sw4})

pc1.on_off()
pc2.on_off()
pc3.on_off()
pc4.on_off()
pc5.on_off()

#pc1.ping('192.168.1.2')
pc5.ping('192.168.1.3', 17)
