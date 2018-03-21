from random import randint
from time import sleep
computador = randint(0, 1)#Faz o computador sortear um número
print('-=-' * 20)
print('Vou pensar em um número! Tente adivinha entre 0 a 5')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))#O jogadaor tenta adivinhar
print('\nPROCESSANDO...')
sleep(2)
if jogador == computador:
    print('\nPARABÉNS! VOCÊ GANHOU :/')
else:
    print('\nVOCê PERDERU! TENE NOVAMENTE :D')
    print('O NÚMERO QUE EU PENSEI FOI {}'.format(computador))

