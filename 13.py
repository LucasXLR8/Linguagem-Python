import os
import time

times = ["Bayern Munique","Borussia Dortmund","RB Leipzig","Barcelona","Real Madrid","Atletico de Madrid","Real Sociedad","Manchester City","Arsenal","Inter de Milão","Napoli",'PSG',"Porto","Copenhague","PSV","Lazio" ]

print('Bem vindo ao Jogo da Adivinhação')
time.sleep(3)
os.system('cls')
print('Tente adivinhar 3 times da Champions League!')

def jogo(times):
    pontos = 0
    
    for x in range(3):
        palpite = input('Digite um time: ').capitalize().strip()
        
        if palpite in times:
            pontos+=1
            print(f'Parabens você acertou o time, você tem {pontos} pontos!')
            times.remove(palpite)
        else:
            print(f'Este time não esta na lista, você tem {pontos} pontos!')
            
jogo(times)
