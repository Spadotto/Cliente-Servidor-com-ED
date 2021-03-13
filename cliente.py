import socket
import random
import sys

sys.setrecursionlimit(10**9)

class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class ListaEncadeada:
      def __init__(self):  
        self.head = None
      
      def inseririnicio(self, data):
        novoNode = Node(data)
        if(self.head):
          aux = self.head
          while(aux.next):
            aux = aux.next
          aux.next = novoNode
        else:
          self.head = novoNode
      
      def imprimirlista(self):
        aux = self.head
        while(aux):
          print(aux.data)
          aux = aux.next

HOST = '127.0.0.1' 
PORT = 80#1024 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
dest = (HOST, PORT) 

client_socket.settimeout(1000) 
client_socket.connect(dest) 

while(True):
    print('Escolha uma das opcoes a seguir: ')
    print('1. Vetor;')
    print('2. Lista Encadeada;')
    print('3. Sair;')
    Msg = input("Escolha: ")
    Msg = str(Msg)
    client_socket.send(Msg.encode('utf-8')) 
    if Msg == '3':
        break;
    
    if Msg == '1':   
        rand = []
        for i in range(25):
            rand.append(random.randrange(0, 100))
        i = 0
        while i < 25:
            rand2 = rand[i]
            rand2 = str(rand2).strip('[]')
            rand2 = rand2.zfill(3)
            i = i + 1
            client_socket.send(rand2.encode('utf-8')) 
            resposta, servidor = client_socket.recvfrom(80) 
            print(resposta.decode())
            
        print('Escolha uma das opcoes a seguir: ')
        print('1. Bubble Sort;')
        print('2. Merge Sort;')
        ordem = input("Escolha: ")
        ordem = str(ordem)
        client_socket.send(ordem.encode('utf-8'))
        try:
            i = 0
            vetor = []
            while i<25:
                resposta, servidor = client_socket.recvfrom(80) 
                vetor.append(resposta.decode())
                msg = 'Dado recebido'
                client_socket.send(msg.encode('utf-8'))
                print('Recebido: ', resposta.decode())
                i = i+1
            print(vetor) 
        except: 
            print('Ocorreu um erro...')

    if Msg == '2':     
        LL = ListaEncadeada()
        x=0
        while x < 25:
            i = [random.randint(0, 100)for i in range(1)]
            LL.inseririnicio(i)
            x = x + 1
        i = 0
        aux = LL.head
        while i < 25:
            rand2 = aux.data
            rand2 = str(rand2).strip('[]')
            rand2 = rand2.zfill(3)
            aux = aux.next
            i = i + 1
            print(rand2)
            client_socket.send(rand2.encode('utf-8')) 
            resposta, servidor = client_socket.recvfrom(80) 
            print(resposta.decode())
            
        print('Escolha uma das opcoes a seguir: ')
        print('1. Bubble Sort;')
        print('2. Merge Sort;')
        ordem = input("Escolha: ")
        ordem = str(ordem)
        client_socket.send(ordem.encode('utf-8'))
        try:
            i = 0
            while i<25:
                resposta, servidor = client_socket.recvfrom(80) 
                LL.inseririnicio(resposta.decode())
                msg = 'Dado recebido'
                client_socket.send(msg.encode('utf-8'))
                print('Recebido: ', resposta.decode())
                i = i+1
            LL.imprimirlista()
        except: 
            print('Ocorreu um erro...')
            
client_socket.close() 

