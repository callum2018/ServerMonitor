import uuid


def get_mac():
    """This code returns mac address of the machine, as a hexadecimal separating bytes with dashes."""
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i: i + 2]
                   for i in range(0, 11, 2))
    return mac

#print ("My Mac Address is; ",get_mac())
