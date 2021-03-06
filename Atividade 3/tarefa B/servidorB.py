# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula  (python 3)
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  
  sentence = sentence.decode('utf-8')
  
  if sentence == "obter arquivo.txt": # filtro de verificacao 
      file = open("arquivo.txt",'r') # aquivo que deve ser aberto 

      for linha in file: # lê a mensagem do arquivo 
        linha = linha.rstrip()
        #print(linha)
      print('Cliente %s enviou: %s, aceito ' % (addr, sentence))    
      connectionSocket.send(linha.encode('utf-8')) # envia para o cliente o texto transformado
  else:
      msg = "Arquivo não existe" 
      print('Cliente %s enviou: %s, negado ' % (addr, sentence))   
      connectionSocket.send(msg.encode('utf-8')) # envia para o cliente o texto transformado    
  #print ('Cliente %s enviou: %s, transformando em: %s' % (addr, sentence, capitalizedSentence))
 
  file.close()  
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor