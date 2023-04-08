'''Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
mês. Calcule e mostre o total de seu salário referido no mês.'''

# entrada
valorhora = float(input('Informe o valor da hora:'));
horas = float(input('Informe a quantidade de horas trabalhadas:'));

# processamento
salario = valorhora * horas

# saída
print('O seu salário mensal é: R$',salario);
