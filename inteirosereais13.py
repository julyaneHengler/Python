'''Faça um progra'ma que peça 2 números inteiros e 1 real. Calcule e mostre o produto do dobro
do primeiro com metade do segundo e a soma do triplo do primeiro com o terceiro.'''

# entrada
n1 = int(input('Digite um número inteiro:'));
n2 = int(input('Digite mais um número inteiro:'));
n3 = float(input('Digite um número real:'));

# processamento
a = (n1 * 2) + (n2 / 2)
b = (n1 * 3) + n3

# saida
print('O produto do dobro do primeiro com metade do segundo é:',a);
print('A soma do triplo do primeiro com o terceiro é:',b);
