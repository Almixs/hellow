import logging
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from device import Router, Smartphone, Smartwatch, Node, Package

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def create_devices():
    logging.debug("Creating devices...")
    router1 = Router("Router1", "00:11:22:33:44:55", "192.168.1.1")
    router2 = Router("Router2", "00:AA:BB:CC:DD:EE", "192.168.2.1")
    router3 = Router("Router3", "00:11:22:33:44:66", "192.168.3.1")
    router4 = Router("Router4", "00:AA:BB:CC:DD:FF", "192.168.4.1")
    router5 = Router("Router5", "00:11:22:33:44:77", "192.168.5.1")

    device1 = Smartphone("Device1", "00:11:22:33:44:56", "192.168.1.2", "Android 12")
    device2 = Smartphone("Device2", "00:11:22:33:44:57", "192.168.2.2", "iOS 15")
    device3 = Smartwatch("Device3", "00:11:22:33:44:58", "192.168.3.2", "v1.0")
    device4 = Smartphone("Device4", "00:11:22:33:44:59", "192.168.4.2", "Android 11")
    device5 = Smartwatch("Device5", "00:11:22:33:44:60", "192.168.5.2", "v2.0")

    logging.debug(f"Created {len([router1, router2, router3, router4, router5])} routers and {len([device1, device2, device3, device4, device5])} devices.")
    return [router1, router2, router3, router4, router5, device1, device2, device3, device4, device5]

def visualize_network(devices):
    logging.debug("Visualizing network...")
    G = nx.Graph()

    num_routers = 5
    angles = np.linspace(0, 2 * np.pi, num_routers, endpoint=False)

    pos = {}

    for i, router in enumerate(devices[:num_routers]):
        x = np.cos(angles[i])
        y = np.sin(angles[i])
        pos[router.name] = (x, y)
        logging.debug(f"Router {router.name} positioned at ({x}, {y})")

    pos["Device1"] = (2.5, 0)
    pos["Device2"] = (0.6, 2)
    pos["Device3"] = (-2, 1.5)
    pos["Device4"] = (-1.8, -1.5)
    pos["Device5"] = (0.7, -2.3)
    logging.debug("Devices positioned relative to routers.")

    G.add_edge("Router1", "Router2")
    G.add_edge("Router2", "Router3")
    G.add_edge("Router3", "Router4")
    G.add_edge("Router4", "Router5")
    G.add_edge("Router5", "Router1")

    G.add_edge("Device1", "Router1")
    G.add_edge("Device2", "Router2")
    G.add_edge("Device3", "Router3")
    G.add_edge("Device4", "Router4")
    G.add_edge("Device5", "Router5")
    logging.debug("Edges added between routers and devices.")

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold',
            edge_color='gray')
    plt.title("Device and Router Network Topology")
    plt.axis('equal')
    plt.show()
    logging.debug("Network visualization complete.")

def main():
    logging.debug("Program started.")
    devices = create_devices()

    nodes = [Node(device) for device in devices]

    nodes[0].connect(nodes[1])
    nodes[1].connect(nodes[2])
    nodes[2].connect(nodes[3])
    nodes[3].connect(nodes[4])
    nodes[4].connect(nodes[5])

    visualize_network(devices)

    package1 = Package(nodes[0], nodes[1], "Hello, Router2!")
    nodes[0].send_packet(package1, nodes[1])

    logging.debug("Program finished.")

if __name__ == "__main__":
    main()
