import logging

class Device:
    def __init__(self, name, device_type, ip_address, mac_address):
        self.name = name
        self.device_type = device_type
        self.ip_address = ip_address
        self.mac_address = mac_address
        logging.info(f"Created {self.device_type}: {self.name}, IP: {self.ip_address}, MAC: {self.mac_address}")

    def __str__(self):
        return f"{self.device_type} {self.name} - MAC: {self.mac_address}, IP: {self.ip_address}"

class Router(Device):
    def __init__(self, device_name, mac_address, ip_address):
        super().__init__(device_name, "Router", ip_address, mac_address)

    def __str__(self):
        return f"Router {self.name} - MAC: {self.mac_address}, IP: {self.ip_address}"

class Smartphone(Device):
    def __init__(self, device_name, mac_address, ip_address, os_version):
        super().__init__(device_name, "Smartphone", ip_address, mac_address)
        self.os_version = os_version

    def __str__(self):
        return f"Smartphone {self.name} - MAC: {self.mac_address}, IP: {self.ip_address}, OS Version: {self.os_version}"

class Smartwatch(Device):
    def __init__(self, device_name, mac_address, ip_address, version):
        super().__init__(device_name, "Smartwatch", ip_address, mac_address)
        self.version = version

    def __str__(self):
        return f"Smartwatch {self.name} - MAC: {self.mac_address}, IP: {self.ip_address}, Version: {self.version}"

class Node:
    def __init__(self, device):
        self.device = device
        self.connections = []
        logging.info(f"Node {self.device.name} created.")

    def connect(self, other_node):
        self.connections.append(other_node)
        logging.info(f"{self.device.name} connected to {other_node.device.name}.")

    def send_packet(self, packet, recipient_node):
        logging.info(f"{self.device.name} sending packet to {recipient_node.device.name}.")
        recipient_node.receive_packet(packet)

    def receive_packet(self, packet):
        logging.info(f"{self.device.name} received packet: {packet.data}")

class Package:
    def __init__(self, source, destination, data):
        self.source = source
        self.destination = destination
        self.data = data
        logging.info(f"Package from {source.device.name} to {destination.device.name} with data: {self.data}")
