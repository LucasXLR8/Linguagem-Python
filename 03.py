import os#Importando biblioteca para limpeza de tela

nome = input('Digite o seu nome: ')
valor01 = float(input('Digite o primeiro numero: '))#O float antes do input serve para que converta oque foi escrito para numero
valor02 = float(input('Digite o segundo numero: '))
os.system('clear')#Comando para limpeza de tela

calculo = valor01*valor02

print(f'{nome}, a multiplicaçao dos dois numero foi {calculo}')