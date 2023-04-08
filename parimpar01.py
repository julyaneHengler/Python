'''Faça um algoritimo para ler um número inteiro e informar se esse número é
par ou ímpar.'''

# entrada
numero = int(input('Informe um número inteiro:'));

# processamento
resto = numero % 2

if resto == 0:
    resposta = 'Par'
else:
    resposta = 'Impar'

# saída
print(resposta);
