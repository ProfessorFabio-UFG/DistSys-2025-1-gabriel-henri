import zmq, time, random
from constPS import *  

context = zmq.Context()
s = context.socket(zmq.PUB)  
p = "tcp://" + HOST + ":" + PORT
s.bind(p)  

topicos = ["temperatura", "umidade", "pressao"]

while True:
    time.sleep(2)  
    topico = random.choice(topicos)
    valor = round(random.uniform(10, 35), 2)
    mensagem = f"{topico.upper()} {valor}"  # ex: "TEMPERATURA 22.5"
    print("Enviando:", mensagem)
    s.send_string(mensagem)
