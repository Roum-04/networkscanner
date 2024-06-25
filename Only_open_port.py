import socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = (input("Enter the host ip"))
def port_scanner(port):
    sock.connect_ex((host,port)) == 0 ,
    print('the port is open'%(port))
    for i in range(1,2000):
        port_scanner(port)
