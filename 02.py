#ATIVIDADE COM CALCULOS ENVOLVENDO PORCENTAGEM

nome = "Lucas"
salarioBruto = 8756

#CALCULO PARA DESCOBRIR A PORCENTAGEM DO IMPOSTO DE RENDA
Ir = (salarioBruto)*0.08
print(f'Imposto de Renda: {Ir}')

#CALCULO PARA DESCOBRIR A PORCENTAGEM DO INSS
inss = (salarioBruto)*0.05
print(f'INSS: {inss}')

#RESULTADO FINAL
salarioLiquido = (salarioBruto-(Ir+inss))
print(f'O salario Liquido de {nome} é: {salarioLiquido}') 