''' Desenvolva um algoritimo que receba as 4 notas bimestrais e ao final exiba a média
aritmética.'''

# entrada
n1 = float(input('Digite a primeira nota:'));
n2 = float(input('Digite a segunda nota:'));
n3 = float(input('Digite a terceira nota:'));
n4 = float(input('Digite a quarta nota:'));

# processamento
media = (n1 + n2 + n3 + n4) / 4;

# saída
print('A média aritmética do aluno é:',media);
