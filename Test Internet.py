import speedtest
import platform
import os
import time
from colors import cores

#chamando a biblioteca de teste de internet
s = speedtest.Speedtest()

#Função para limpar o CMD
def limpar():
    if platform.system() == 'Windows':
        os.system('cls')

#Loop
while True:
    limpar()
    print('{}Teste de Internet{}\n'.center(40).format(cores['azul'], cores['limpa']))

    #Escolha de iniciar ou sair
    esc = int(input('Pressione 1 para Iniciar e 2 para Sair: '))
    
    if esc == 1:
        print('{}Iniciado\n{}'.format(cores['verde'], cores['limpa']))
        
    elif esc == 2:
        print('{}Encerrado{}'.format(cores['vermelho'], cores['limpa']))
        break
    elif(esc != 1 and esc != 2):
        print('{}Digite corretamente o que se pede!{}'.format(cores['vermelho'], cores['limpa']))
        break

    print('{}Processando...{}\n'.format(cores['amarelo'], cores['limpa']))

    #variáveis como testes de velocidade de download, upload e ping
    dspeed = s.download() / 1000000
    uspeed = s.upload() / 1000000
    ping = round(s.results.ping)

    #print com as velocidades
    print('{}Velocidade de Download: {:.2f} Mbps{}'.format(cores['verde'], dspeed, cores['limpa']))
    print('{}Velocidade de Upload: {:.2f} Mbps{}'.format(cores['verde'], uspeed, cores['limpa']))
    print('{}Ping: {}{}'.format(cores['verde'], ping, cores['limpa']))

#escolha se deseja testar novamente ou não
    dnv = str(input('{}Deseja testar novamente ? S/N: {}'.format(cores['azul'], cores['limpa']))).lower()

    if dnv == 's':
        print('{}Reiniciando...{}'.format(cores['verde'], cores['limpa']))
        time.sleep(1)
        limpar()
    elif dnv == 'n':
        print('{}Encerrado{}'.format(cores['vermelho'], cores['limpa']))
        break
    else:
        print('{}Digite corretamente !{}'.format(cores['vermelho'], cores['limpa']))