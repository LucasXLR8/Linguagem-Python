#ATIVIDADE ENVOLVENDO NOTAS E IF ELSE
import os

nome = input('Digite o seu nome: ')
uni1 = float(input('Digite a nota da primeira unidade: '))
uni2 = float(input('Digite a nota da segunda unidade: '))
uni3 = float(input('Digite a nota da terceira unidade: '))
os.system('cls')

media = (uni1+uni2+uni3)/3

if media >= 7:
    print(f'{nome}, sua média foi: {media:.1f}')
    print('Parabéns Brabo(a)')
elif media >=5 and media < 7:#O elif é o else if do python
    print(f'{nome}, sua média foi: {media:.1f}')
    print('Você se qualificou para prova final')
else:
    print(f'{nome}, sua média foi: {media:.1f}')
    print('Vacilou zé da manga')   