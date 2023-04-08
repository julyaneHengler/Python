'''Escreva um algoritmo que leia dois valores inteiros e imprimir uma das três mensagens
a seguir:
‘Números iguais’, caso os números sejam iguais
‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
‘Segundo maior’, caso o segundo seja maior que o primeiro.'''

# entrada
n1 = int(input('Digite um valor:'));
n2 = int(input('Digite outro valor:'));

# processamento
if n1 == n2:
    resposta = 'Números iguais'
else:
    if n1 > n2:
        resposta = 'Primeiro é maior'
if n2 > n1:
    resposta = 'Segundo é maior'

# saida
print (resposta);

