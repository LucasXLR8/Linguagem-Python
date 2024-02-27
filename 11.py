import os
import random

secreto = random.randint(1,100)

tentativas = 1

while True:
    palpite = int(input('Digite um numero entre 1 e 100: '))
    os.system('cls')
    
    if palpite == secreto:
        print(f'Parabens você acertou o numero secreto em {tentativas} tentativas')
        break
    elif palpite < secreto:
        print('O numero secreto é maior!')
        tentativas += 1
    else:
        print('O numero secreto é menor!')
        tentativas += 1