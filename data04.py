'''Desenvolva um algoritmo que receba o dia da semana (número) e informe o
dia da semana (literal).

DIA	DESCRIÇÃO
1	Segunda-Feira
2	Terça-Feira
3	Quarta-Feira
4	Quinta-feira
5	Sexta-Feira
6	Sábado
7	Domingo '''

#entrada
data = int(input('Informe o número do dia da semana:'));

# processamento
if data == 1:
    resposta = ('Segunda-Feira');
else:
    if data == 2:
        resposta = ('Terça-Feira');
    else:
            if data == 3:
                resposta = ('Quarta-Feira');
            else:
                if data == 4:
                    resposta = ('Quinta-Feira');
                else:
                    if data == 5:
                        resposta = ('Sexta-Feira');
                    else:
                        if data == 6:
                            resposta=('Sabado');
                        else:
                            if data == 7:
                                resposta = ('Domingo');
                                
#saida
print(resposta);

