import requests
import socket
import ipaddress
import configparser

config = configparser.ConfigParser()

config.read("config.conf")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('1.1.1.1', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
ip = get_ip()
print(ip, ipaddress.ip_address(ip).is_private)

def add_record():
    record = {}
    record["type"] = "A"
    record["name"] = 