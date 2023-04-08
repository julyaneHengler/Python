'''Escreva um algoritmo que leia o nome de 2 times e o número de gols marcados na partida
(para cada time).Escrever o nome do vencedor. Caso não haja vencedor deverá ser
impressa a palavra EMPATE.'''

# entrada
time1 = input('Informe o nome do time:');
gols1 = int(input('Informe a quantidade de gols feitos por esse time:'));
time2 = input('Informe o nome do outro time:');
gols2 = int(input('Informe a quantidade de gols feitos por esse time:'));

# processamento
if gols1 > gols2:
    resposta = f'O vencedor é o {time1}, com {gols1} gols'
if gols2 > gols1:
    resposta = f'O vencedor é o {time2}, com {gols2} gols'
else:
    if gols1 == gols2:
        resposta = 'Empate'

# saida
print(resposta);
