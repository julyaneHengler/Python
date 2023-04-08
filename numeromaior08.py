'''Escrever um algoritmo que leia dois valores inteiros distintos e informe qual é o maior.'''

# entrada
n1 = int(input('Digite um número:'));
n2 = int(input('Digite outro número:'));

# processamento
if n1 > n2:
    resposta = 'O número',n1,'é maior que o número',n2;
else:
    resposta = 'O número',n2, 'é maior que o número',n1;

# Saída
print(resposta);
