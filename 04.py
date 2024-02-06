#ATIVIDADE COM CALCULOS ENVONVENDO MULTIPLICAÇAO E DIVISAO
import os

nome = input('Digite o seu nome: ')
peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
os.system('clear')

imc = peso/(altura*altura)
print(f'{nome}, o seu IMC é {imc:.2f}')