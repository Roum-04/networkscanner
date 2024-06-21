from socket import *
import optparse
from threading import *
def connScan(tgthost,tgtport):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((tgthost,tgtport))
        print('the port is open'%(tgtport))
    except:
        print('the port is closed'%(tgtport))
    finally:
        sock.close()
        def portscan(tgthost,tgtports):  
            try:
                tgtIP=gethostbyname(tgthost) 
            except:
                print('unknown host %s' %(tgthost)) 
            try:
                tgtName=gethostbyaddr(tgtIP)
                print('scan result for :'+tgtName[0])
            except:
                print('scan result for :'+tgtIP)
                setdefaulttimeout(1)
                for tgtport in tgtports:
                    t= Thread(target=connScan,args=(tgthost,int(tgtport)))
                    t.start()
                    def main():
                        parser=optparse.optionparser('usage of the program :'+' -H <target host> -p<target port>')
                        parser.add_option('-H',dest='tgtHost',type='String',help='specifing target host')
                        parser.add_option('-p',dest='tgtHost',type='String',help='specifing target port separated by comma')
                        (options,args)=parser.parse_args()
                        tgtHost=options.tgtHost
                        tgtports= str(options.tgtport).spilt(',')
                        if(tgthost == None)|(tgtports[0]== None):
                            print (parser.usage)
                            exit(0)
                            portScan(tgtHost,tgtports)
                            if__name__=='__main__'
                            main()





  # 1> this is basically a advanced port scanner in which there are three library in which socket is used to scan the port and optprase is used
  # to give option to for the input and threading library is used to execute multiple thread in the scanner.
  # 2> In main function we specify the optparse library in which we use a method called as optionparser which is used to  give option when the user enter
  # wrong option and add_option is used to add argument in the option.
  # 3> if(tgthost == None)|(tgtports[0]== None): is used to specify if the user give nothing then pass parser.usage
  # 4> def portscan(tgthost,tgtports): in this method we specify if the user give input in domain name then output will be produced
  # 5> gethostbyname and  gethostbyaddr are used to get input of host  in domain name and ip address               
  # 6> def connScan(tgthost,tgtport): this method is used to scan and give output                