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
                        parser.add_option('-p',dest='tgtHost',type='String',help='specifing target port separted by comma')
                        (options,args)=parser.parse_args()
                        tgtHost=options.tgtHost
                        tgtports= str(options.tgtport).spilt(',')
                        if(tgthost == None)|(tgtports[0]== None):
                            print (parser.usage)
                            exit(0)
                            portScan(tgtHost,tgtports)
                            if__name__=='__main__'
                            main()
        # this is network scanner in which in which the there is specialised help otion to tell about how 
        # to put input in the the input
