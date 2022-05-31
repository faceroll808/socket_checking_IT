import socket
target="127.0.0.1"
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
for port in range (1,1024):
    result = portscan(port)
    if result:
        print("port {} is open!".format(port))
    else:
        print("port {} is closed!".format(port))