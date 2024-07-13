import socket as sk

s = sk.socket(sk.AF_INET ,  sk.SOCK_DGRAM)

target_ip = "127.0.0.1"
port_no = 2525

target_address = (target_ip,port_no)


quiet= True
while quiet:
    message = input("plz enter the message : ")
    message_encrypt = message.encode('ascii')
    s.sendto(message_encrypt,target_address)

    user_input = input("do you want to quiet it press Y/y : ")
    if user_input =="Y" or user_input =="y":
        quiet = False