'''Faça um algoritmo para ler duas variáveis inteiras A e B e garantir que A e B
fiquem em ordem crescente, ou seja, a variável A deverá armazenar o menor valor
fornecido e a variável B o maior.'''

# entrada
a = int(input('Digite um valor para A:'));
b = int(input('Digite um valor para B:'));

# processamento
if a > b:
    aux = a
    a = b
    b = aux

# saída
print('A =',a,'B =',b);
