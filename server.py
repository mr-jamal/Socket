import socket

ob=socket.socket()
ob.bind(('localhost',2301))
ob.listen(4)
clientobject,add=ob.accept()
print("server is ready to accept connection")
print('connected with this address',add)
#to recirvr thr data from client
'''gotmsg=clientobject.recv(1024)
gotmsg.decode('utf-8')
print(gotmsg)
#ob.close()'''

conn=True
while conn:
    gotmsg=clientobject.recv(1024)
    gotmsg.decode('utf-8')
    print(gotmsg)
    #ob.close()
    if len(gotmsg)==0:
        conn=False
        ob.close()
