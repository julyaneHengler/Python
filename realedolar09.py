'''Elaborar um algoritimo que efetue a apresentação do valor da conversão em real (R$) de
um valor lido em dólar (US$). O algoritimo deverá solicitar o valor da cotação do dólar e
também a quantidade de dólares disponiveís com o usuário.'''


cotacao = float(input('Informe o valor da cotação do dólar:'));
qtdDolares = float(input('informe a quantidade de dólares disponiveis:'));

conversaoparareal = cotacao * qtdDolares;

print('O valor convertido em real é R$',conversaoparareal);
