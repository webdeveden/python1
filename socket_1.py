import socket #import the socket library

url= 'data.pr4e.org'
prt= 80

mysock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)#make a socket as a file handle but no data associated with it yet
#mysock.connect(('data.pr4e.org',80))#connecting the socket to a destination on the internet
mysock.connect((url,prt))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()#sending a http command,'\n\n'end line followed by a blank line
#.encode()= converting unicode to utf code
mysock.send(cmd) #after making the connection we send it and wait for the response

while  True:
    data=mysock.recv(512)#asking up to 512 characters
    if len(data)<1:# if nothing on the data
        break# quit
    print(data.decode())#.decode() convert it unicode again so we can read it
mysock.close()# done, close the connection
