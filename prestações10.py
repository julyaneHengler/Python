'''A loja Mamão com Açucar está vendendo seus produtos em 5 prestações sem juros. Faça um
algotitimo que receba o valor de uma compra e mostre o valor das prestações.'''

# entrada
compra = float(input('Informe o valor da compra:'));

# processamento
prestacoes = compra / 5

# saída
print('O valor das prestações é de R$',prestacoes);
