'''Faça um algoritmo para ler um salário e atualizá-lo de acordo com a tabela
abaixo.
FAIXA SALARIAL	AUMENTO
Até 600,00		30%
600,01 a 1.100,00	25%
1100,01 a 2.400,00	20%
2400,01 a 3.550,00	15%
Acima de 3.550,00	10%'''

#entrada
salario = float(input('Informe o salário do funcionário: R$'));

# processamento
if salario <= 600.00:
    aumento= salario * 30 / 100
    salariofinal= salario + aumento
    mensagem = f'O funcionário tem o salário de {salario}. Seu novo salário é {salariofinal}, o aumento foi de 30%'
else:
    if salario >= 600.01:
      if salario <= 1100.00:
        aumento = salario * 25 / 100
        salariofinal= salario + aumento
        mensagem = f' O funcionário tem o salário de {salario}. Seu novo salário é {salariofinal}. O aumento foi de 25%'
        if salario >= 1100.01:
            if salario <=2400.00:
                aumento= salario * 20 / 100
                salariofinal= salario + aumento
                mensagem = f'O funcionário tem o salário de {salario}. Seu novo salário é {salariofinal}. O aumento foi de 20%'
                if salario >= 2400.01:
                    if salario <= 3550.00:
                        aumento = salario * 15 / 100
                        salariofinal = salario + aumento
                        mensagem = f'O funcionário tem o salário de {salario}. Seu novo salário é {salariofinal}. O aumento foi de 15%.'
                        if salario >= 3550.01:
                            aumento = salario * 10 / 100
                            salariofinal = salario + aumento
                            mensagem = f'O funcionário tem o salário de {salario}. Seu novo salário é {salariofinal}. O aumento foi de 10%.'

#
 saida
print(mensagem);



