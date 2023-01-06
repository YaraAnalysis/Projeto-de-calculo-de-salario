#valor_hora = float(input('Informe o valor da sua hora trabalhada em reais: '))
#qtd_horas_mes = float(input('Informe o quantidade de horas trabalhadas no mês: '))
#salario_bruto = qtd_horas_mes * valor_hora

#print('Salário do mês: R$',{salario_bruto})
#print('Descontos aplicados: ')

funcionarios = []
salarios = []

nome = input('Digite o NOME do funcionário: ')
funcionarios.append(nome)
salario = float(input('Informe o VALOR DO SALÁRIO mensal em reais: '))
salarios.append(salario)

repetir = input('Deseja cadastrar um funcionário? (S/N)')
while repetir == 'S':
    nome = input('Digite o NOME do funcionário: ')
    funcionarios.append(nome)
    salario = float(input('Informe o VALOR DO SALÁRIO mensal em reais: '))
    salarios.append(salario)
    repetir = input('Deseja cadastrar OUTRO funcionário? (S/N)')

print(funcionarios)
print(salarios)

qtd_funcionarios = len(funcionarios)
print(qtd_funcionarios)
i_funcionario = 0
liquido = 3

if salarios[i_funcionario] <= 900.0:
    percentual = 0
elif salario <= 1500.0:
    percentual = 0.05
elif salario <= 2500.0:
    percentual = 0.1
else:
    percentual = 0.2

while i_funcionario < qtd_funcionarios:
    print('Funcionário: {} | Salário Bruto: R$ {} | Salário Líquido: R${}.'.format(funcionarios[i_funcionario], salarios[i_funcionario], liquido))
    i_funcionario +=1
