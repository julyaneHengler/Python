'''Faça um algoritmo que receba um número e diga se este número está no intervalo entre
100 e 200.'''

# entrada
numero = int(input('Digite um número:'));

# processamento
if numero > 100 < 200:
    resposta = ('Este número está no intervalo entre os números 100 e 200.')
else:
    resposta = ('Este número não está no intervalo entre os números 100 e 200.')

# saída
print(resposta);
