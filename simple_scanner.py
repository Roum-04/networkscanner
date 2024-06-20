import socket
sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = input("Enter the ip address of host =")
port=int(input("Enter the port number = "))
def port_scanner(port):
    if sock.connect_ex(host,port):
        print("the port is closed"%(port))
    else:
        print("the port is open"%(port))
        port_scanner(port)