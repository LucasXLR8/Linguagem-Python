pessoas = ['Paloma','Isadora','Lucas','Junior','Leo']

total = len(pessoas)

#Primeira forma de fazer o laço FOR
for x in range(total):
    if pessoas[x].startswith('L'):
        print(pessoas[x])

#Segunda forma de fazer o laço FOR
for x in pessoas:
    if x.startswith('L'):
        print(x)