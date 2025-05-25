import zmq, sys
from constPS import *  # HOST e PORT

context = zmq.Context()
s = context.socket(zmq.SUB)  # cria socket subscriber
p = "tcp://" + HOST + ":" + PORT
s.connect(p)

# Permite passar o tópico por argumento ou usar TEMPERATURA como padrão
topico = sys.argv[1] if len(sys.argv) > 1 else "TEMPERATURA"
s.setsockopt_string(zmq.SUBSCRIBE, topico.upper())

print(f"Inscrito no tópico: {topico.upper()}")
for i in range(10):  # limita para 10 mensagens
    msg = s.recv()
    print("Recebido:", msg.decode())
