funcionarios = []
salarios = []
liquidos = []
i_funcionario = 0

#nome = input('Digite o NOME do funcionário: ')
#funcionarios.append(nome)
#salario = float(input('Informe o VALOR DO SALÁRIO mensal em reais: '))
#salarios.append(salario)

repetir = input('Deseja cadastrar UM funcionário? (S/N)')
while repetir == 'S':
    nome = input('Digite o NOME do funcionário: ')
    funcionarios.append(nome)
    salario = float(input('Informe o VALOR DO SALÁRIO mensal em reais: '))
    salarios.append(salario)
    repetir = input('Deseja cadastrar OUTRO funcionário? (S/N)')
    if salario <= 900.0:
        ir = 0
    elif salario <= 1500.0:
        ir = 0.05 * salario
    elif salario <= 2500.0:
        ir = 0.1 * salario
    else:
        ir = 0.2 * salario
    sindicato = salario * 0.03
    inss = salario * 0.1
    descontos = ir + inss + sindicato
    sal_liquido = salario - descontos
    liquidos.append(sal_liquido)

qtd_funcionarios = len(funcionarios)

taxas = '\nDescontos aplicados: \n Sindicato: 3% \n INSS: 10%'
taxas_ir = '\nBase de cálculo do IR:\n Salário Bruto até 900 (inclusive) - isento \n Salário Bruto até 1500 (inclusive) - desconto de 5% \n Salário Bruto até 2500 (inclusive) - desconto de 10% \n Salário Bruto acima de 2500 - desconto de 20%\n'
print(taxas)
print(taxas_ir)

while i_funcionario < qtd_funcionarios:
    print('Funcionário: {} | Salário Bruto: R$ {} | Salário Líquido: R${}.'.format(funcionarios[i_funcionario], salarios[i_funcionario], liquidos[i_funcionario]))
    i_funcionario += 1
