'''Escreva um algoritmo que leia 3 valores inteiros
(considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.'''

# entrada
n1 = int(input('Digite um número:'));
n2 = int(input('Digite um número diferente do anterior:'));
n3 = int(input('Digite outro número diferente dos dois anteriores:'));

# processamento
if n1 > n2 and n3 > n2:
    soma = n1 + n3
    resposta = f'A soma dos dois números maiores é {soma}'
else:
    if n1 > n3 and n2 > n3:
        soma = n1 + n2
        resposta = f'A ssoma dos dois números maiores é {soma}'
if n2 > n1 and n3 > n1:
    soma = n2 + n3
    resposta = f'A soma dos dois números maiores é {soma}'


# saída
print(resposta);
