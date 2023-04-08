''' Desnvolva um algoritimo que receba dois números e ao final exiba a soma, a subtração,
a multiplicação e a divisão  dos números lidos. '''

# entrada
n1 = float(input('Digite um número: '));
n2 = float(input('Digite um segundo número: '));

# processamento
soma = n1 + n2;
sub = n1 - n2;
multi = n1 * n2;
div = n1 / n2;

# saída
print('O resultado da soma dos dois números é:',soma);
print('O resultado da subtração dos dois números é:',sub);
print('O resultado da multiplicação dos dois números é:',multi);
print('O resultado da divisão dos dois números é:',div);

