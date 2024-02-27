valores = [22,33,44,23,26,29,67,56,45,46,32,11,17]

impares=[]

for x in valores:
    resto = x%2
    if resto != 0:
        impares.append(x)
        
somatorio = sum(valores)
media = somatorio/13

print(f'Numeros impares são: {impares}')
print(f'A soma total foi: {somatorio}')
print(f'A media da soma foi: {media:.1f}:')