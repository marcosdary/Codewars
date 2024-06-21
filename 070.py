import ipaddress

def is_valid_IP(strng):
    try:
        ipaddress.ip_address(strng)
        return True
    except ValueError:
        return False
    
ip = "192.168.0.1"
print(is_valid_IP(ip))