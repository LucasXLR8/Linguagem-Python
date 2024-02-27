numeros = [5,-3,10,8,-2,15,7,-9,4,6]

positivo=[]
negativo=[]

for x in numeros:
    if x >= 0:
        positivo.append(x)
    else:
        negativo.append(x)
        
print(f'Os numeros positivos são: {positivo}')
print(f'Os numeros negativos são: {negativo}')
print(f'O total de numeros positivos é: {len(positivo)}')
print(f'O total de numeros negativos é: {len(negativo)}')