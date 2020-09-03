import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:7777")

while True:
    msg = socket.recv()
    print('from client : ' , msg)
    smsg = input(' enter your message here : ')
    socket.send_string(smsg)
    print ('')