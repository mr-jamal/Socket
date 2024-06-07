import socket

ob=socket.socket()
ob.connect(('localhost',2301))
conn=True
while conn:
    msg=input("Enter Your message\n")
    ob.send(msg.encode('utf-8'))
    if msg=='no':
        conn=False
        ob.close()
