'''Um determinado clube de futebol pretende classificar seus atletas em categorias e
para isto ele contratou um programador para criar um programa que executasse esta tarefa.
Para isso o clube criou uma tabela que continha a faixa etária do atleta e sua categoria.
A tabela está demonstrada abaixo:
IDADE 		CATEGORIA
De 05 a 10	Infantil
De 11 a 15	Juvenil
De 16 a 20 	Junior
De 21 a 25 	Profissional
Construa um programa que solicite o nome e a idade de um atleta e imprima a sua categoria.'''

# entrada
nome = input('Informe seu nome:');
idade = int(input('Informe sua idade:'));

# processamento
if idade >= 5:
    if idade <= 10:
        resposta = 'O atleta está na categoria infantil.'
else:
    if idade >= 11:
        if idade <= 15:
            resposta = 'O atleta está na categoria juvenil.'
else:
    if idade >= 16:
        if idade <= 20:
            resposta = 'O atleta está na categoria junior.
else:
    if idade >= 21:
        if idade <= 25:
            resposta = 'O atleta está na categoria profissional.'

# saída
print(resposta);
