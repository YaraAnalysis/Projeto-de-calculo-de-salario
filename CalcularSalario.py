#valor_hora = float(input('Informe o valor da sua hora trabalhada em reais: '))
#qtd_horas_mes = float(input('Informe o quantidade de horas trabalhadas no mês: '))
#salario_bruto = qtd_horas_mes * valor_hora

#print('Salário do mês: R$',{salario_bruto})
#print('Descontos aplicados: ')

funcionarios = []
salarios = []

nome = input('Digite o NOME do funcionário: ')
funcionarios.append(nome)
salario = float(input('Informe o valor SALÁRIO mensal em reais: '))
salarios.append(salario)

repetir = input('Deseja cadastrar OUTRO funcionário? (S/N)')
while repetir == 'S':
    nome = input('Digite o nome do funcionário: ')
    funcionarios.append(nome)
    salario = float(input('Informe o valor salário mensal em reais: '))
    salarios.append(salario)
    repetir = input('Deseja cadastrar outro funcionário? (S/N)')

print(funcionarios)
print(salarios)