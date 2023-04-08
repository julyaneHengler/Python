'''Faça um algoritimo que receba o preço custo de um produto e mostre o valor da venda.
Sabe- se que o preço de custo receberá um acréscimo de acordo com um percentual informado
pelo usuário.'''

# entrada
precocusto = float(input('Informe o preço custo do produto:'));
percentual = float(input('Informe o percentual de acréscimo:'));

# processamento
acrescimo = (precocusto * percentual) / 100;
valorvenda = precocusto + acrescimo;

# saída
print('O valor de venda do produto é: R$', valorvenda);
