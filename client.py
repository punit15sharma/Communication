import zmq
context = zmq.Context()
socket=context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:7777")

while True:
    msg= input('enter your msg here :')
    socket.send_string(msg)
    print('sending', msg )
    print ('From Server : ', socket.recv() )
    print('')
