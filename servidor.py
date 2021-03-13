import socket
import time
import sys

sys.setrecursionlimit(10**9)

def memory_usage_psutil():
    import psutil
    import os
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem

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

 #Bubble Sort
def BubbleSort(self):
     fim = None
     while fim != self.head.next:
            a = self.head
            while a.next != fim:
                b = a.next
                if a.data > b.data:
                    a.data, b.data = b.data, a.data
                a = a.next
            fim = a

def bubble_sort(vetor):
    tamanho = len(vetor)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(tamanho):
            if vetor[i] > vetor[i+1]:
                vetor[i], vetor[i+1] = vetor[i+1],vetor[i]
                ordenado = False      
                print(vetor[i])
                
 #Merge Sort
def SortedMerge(a, b):
        if a is None:
            return b
        elif b is None:
            return a
    
        if a.data <= b.data:
            aux = a
            aux.next = SortedMerge(a.next, b)
        else:
            aux = b
            aux.next = SortedMerge(a, b.next)
    
        return aux
    
def DivideLista(head):        
            esquerda = head
            direita = head
        
            if direita:
               direita = direita.next
            while direita:
                direita = direita.next
                if direita:
                    esquerda = esquerda.next
                    direita = direita.next
         
            aux = esquerda.next
            esquerda.next = None
        
            return head, aux

def MergeSort(head):
        if head is None or head.next  is None:
            return head
    
        esquerda, direita = DivideLista(head)
        esquerda = MergeSort(esquerda)
        direita = MergeSort(direita)
    
        return SortedMerge(esquerda, direita)

def mergeSort(vetor):
    if len(vetor)>1:
        meio = len(vetor)//2
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        i=0
        j=0
        k=0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k]=esquerda[i]
                i=i+1
            else:
                vetor[k]=direita[j]
                j=j+1
            k=k+1

        while i < len(esquerda):
            vetor[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            vetor[k]=direita[j]
            j=j+1
            k=k+1

HOST = 'localhost'
PORT = 80#1024 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
orig = (HOST, PORT) 

server_socket.bind(orig) 
server_socket.listen(1) 

print('Aguardando conexões...')

while True: 
    socket, cliente = server_socket.accept()
    while True: 
        msg = socket.recv(80)
        est = msg.decode()
        print('Escolhido: ' , msg.decode())
        
        if  est == '1':
            vetor = []
            i = 0
            while i<25:
                rand = socket.recv(80)
                vetor.append(rand.decode())
                print('Recebido: ' , rand.decode())
                msg = 'Dado recebido'
                socket.send(msg.encode())
                i = i+1
                if not rand : break
                
            print(vetor)
            ordem = socket.recv(80)
            print('Ordenacao: ' , ordem.decode())
            if ordem.decode() == '1':
                mem = memory_usage_psutil()
                ini = time.time() 
                bubble_sort(vetor)
                print('Vetor ordenado: ')
                print(vetor)
                fim = time.time()
                try:
                    i = 0
                    while i < 25:
                        rand2 = vetor[i]
                        i = i + 1
                        socket.send(rand2.encode('utf-8')) 
                        msg2 = socket.recv(80)
                        print(msg2.decode(), ' - ', rand2)
                    
                except:
                   print('Erro ao responder.')
                   break
            
            elif ordem.decode() == '2':
                mem = memory_usage_psutil()
                ini = time.time()            
                mergeSort(vetor)
                print('Vetor ordenado: ')
                print(vetor)
                fim = time.time()
                try:
                    i = 0
                    while i < 25:
                        rand2 = vetor[i]
                        i = i + 1
                        socket.send(rand2.encode('utf-8')) 
                        msg2 = socket.recv(80)
                        print(msg2.decode(), ' - ', rand2)
                except:
                   print('Erro ao responder.')
                   
        if  est == '2':
            LL = ListaEncadeada()
            i = 0
            while i<25:
                rand = socket.recv(80)
                LL.inseririnicio(rand.decode())
                print('Recebido: ' , rand.decode())
                msg = 'Dado recebido'
                socket.send(msg.encode())
                i = i+1
                if not rand : break
            
            print('Lista: ')
            LL.imprimirlista
            aux = LL.head
            ordem = socket.recv(80)
            print('Ordenacao: ' , ordem.decode())
            if ordem.decode() == '1':
                mem = memory_usage_psutil()
                ini = time.time() 
                BubbleSort(LL)
                print('Lista ordenada: ')
                aux = LL.head
                fim = time.time()
                try:
                    i = 0
                    while i < 25:
                        rand2 = aux.data
                        i = i + 1
                        aux = aux.next
                        socket.send(rand2.encode('utf-8')) 
                        msg2 = socket.recv(80)
                        print(msg2.decode(), ' - ', rand2)
                except:
                   print('Erro ao responder.')
                   break
            
            elif ordem.decode() == '2':
                mem = memory_usage_psutil()
                ini = time.time() 
                LL.head = MergeSort(LL.head)
                print('Lista ordenada: ')
                LL.imprimirlista
                aux = LL.head
                fim = time.time()
                try:
                    i = 0
                    while i < 25:
                        rand2 = aux.data
                        i = i + 1
                        aux = aux.next
                        socket.send(rand2.encode('utf-8')) 
                        msg2 = socket.recv(80)
                        print(msg2.decode(), ' - ', rand2)
                        
                except:
                   print('Erro ao responder.')
                   
        if est == '3':
            print('Conexão Finalizada...'), cliente 
            break
        
        print('Tempo de execucao: ', fim-ini)
        print('Uso de memoria: ', mem)
    break


