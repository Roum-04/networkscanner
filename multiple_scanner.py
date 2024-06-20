import socket
sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = input("Enter the ip address of host =")
def port_scanner(port):
    if sock.connect_ex(host,port):
        print('the port is closed'%(port))
    else:
        print('the port is open'%(port))
        for i  in range(1,1000):
            port_scanner(port)