#ATIVIDADE DE IMC COM IF ELSE
import os

nome = input('Digite o seu nome: ')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
os.system('clear')

imc = peso/(altura*altura)

if imc < 18.5:
    print(f'{nome}, o seu IMC deu: {imc:.1f}')
    print('Você esta abaixo do peso frangote')
elif imc >= 18.5 and imc < 25.0:
    print(f'{nome}, o seu IMC deu: {imc:.1f}')
    print('Você esta com peso normal!')
elif imc >= 25.0 and imc < 30.0:
    print(f'{nome}, o seu IMC deu: {imc:.1f}')
    print('Ta pesado ze da manga, va treinar!')
elif imc >= 30.0:
    print(f'{nome}, o seu IMC deu: {imc:.1f}')
    print('Para de comer FastFood seu gorducho!')