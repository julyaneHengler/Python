'''De acordo com a tabela abaixo, desenvolva um algoritmo que leia um código do produto
informado pelo usuário e informe a descrição do lanche.
CÓDIGO	DESCRIÇÃO DO PRODUTO
100		X-Salada com coca-cola.
200		Hot dog com suco de laranja
300		Sanduiche natural com suco de uva.
400		Misto Quente com fanta laranja.
500		Pão com manteiga com café.
600		Pão com manteiga na chapa com café com leite.

Qualquer outro código diferente dos códigos da tabela, informar a mensagem "Código informado
inválido."'''

# entrada
codigo = int(input('Digite o código do produto:'));

# processamento
if codigo == 100:
    resposta = ('X- Salada com coca- cola');

    if codigo == 200:
        resposta = ('Hot dog com suco de laranja');

    if codigo == 300:
        resposta = ('Sanduiche natural com suco de uva');

    if codigo == 400:
        resposta = ('Misto Quente com fanta laranja');

    if codigo == 500:
        resposta = ('Pão com manteiga, e café');

    if codigo == 600:
        resposta = ('Pão com manteiga, na chapa, e café com leite');

else:
   resposta = ('O código informado está inválido.');

#saída
print(resposta);
 
 
 
