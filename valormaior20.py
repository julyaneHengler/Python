'''Desenvolva um algoritmo que leia três valores inteiro
informado pelo usuário e ao final exiba o maior valor entre eles.'''

# entrada
n1 =  int(input('Digite um número:'));
n2 = int(input('Digite mais um número:'));
n3 = int(input('Digite outro número:'));

# processamento
if n1 > n2 and n3:
    resposta= f'O maior valor é {n1}'
else:
    if n2 > n1 and n3:
        resposta = f'O maior valor é {n2}'
if n3 > n1 and n2:
    resposta = f'O maior valor é {n3}'

# saida
print(resposta);
