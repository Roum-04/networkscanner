import socket
def  retbanner(ip,port):
   sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   sock.connect(ip,port)
   banner= sock.recv(1024)
   def main():
     ip= input("Enter the target ip address")
     port= int(input("Enter the port you want to scan"))
     banner = retbanner(ip,port)
     if banner:
        print("the ip is"+ip+"and banner is "+banner)
        main()
    

