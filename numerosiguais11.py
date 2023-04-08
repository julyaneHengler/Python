'''Faça um algoritmo para ler dois números inteiros e informar se estes
números são iguais ou diferentes.'''

# entrada
n1 = int(input('Digite um número:'));
n2 = int(input('Digite outro número:'));

# processamento
if n1 == n2:
    resposta = 'Ambos os números são iguais.'
else:
    resposta = 'Os números são diferentes.'

# saída
print(resposta);
