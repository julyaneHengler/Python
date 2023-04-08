'''Desenvolva um algoritimo que leia o nome de um vendedor, o seu salário fixo e o total de
vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o seu nome, o salário fixo e o salário no fim do mês.'''

# entrada
nome = input('Informe o nome do vendodor:');
salariofixo = float(input('Informe seu salário fixo:'));
totalvendas = float(input('Informe o total de vendas do vendedor:'));

# processamento
comissao = (totalvendas * 15) / 100;
salariofinal = salariofixo + comissao;

# saida
print('O vendedor',nome,', possui o salário fixo de R$',salariofixo,', e seu salário no final do mês é de R$',salariofinal);
