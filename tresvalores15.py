'''Escreva um algoritmo que leia 3 valores inteiros (considere que não serão
informados valores iguais)e escrever o maior deles.'''

# entrada
n1 = int(input('Digite um número:'));
n2 = int(input('Digite um número diferente do anterior:'));
n3 = int(input('Digite outro número diferente dos dois anteriores:'));

# processamento
if n1 > n2 and n3:
    resposta = f'O maior número é {n1}'
else:
    if n2 > n1 and n3:
        resposta = f'O maior número é {n2}'
        
if n3 > n1 and n2:
    resposta = f'O maior número é {n3}'

# saída
print(resposta);
