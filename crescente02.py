'''Faça um algoritimo para ler duas variáveis inteiras, A e B, e garantir que fiquem em ordem
crescente, ou seja, a variável A deverá armazenar o menor valor fornecido e a variável B o
maior.'''

# entrada
A = int(input('Digite um valor inteiro:'));
B= int(input('Digite outro valor inteiro:'));

# processamento
if A > B:
    resposta = ('O valor de A é:',B);
    resposta1 = ('O valor de B é:',A);
else:
    resposta = ('O valor de A é:',A);
    resposta1 = ('O valor de B é:',B);

# saída
print(resposta);
print(resposta1);
