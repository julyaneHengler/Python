''' Escreva um algoritimo para determinar o consumo médio de um automóvel sendo fornecida
a distância total percorrida e o total de combustível gasto.'''

# entrada
distancia = float(input('Informe a distância total percorrida pelo automóvel:'));
combustivel = float(input('Informe o total de combustível gasto:'));

# processamento
consumomedio = distancia / combustivel;

#saída
print('O consumo médio de um automóve é:',consumomedio);
