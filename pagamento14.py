'''Faça um algoritmo que receba o valor da venda informado pelo usuário, e exiba
o valor da compra de acordo com as condições de pagamento listadas abaixo:
1 - Venda a Vista - desconto de 10%
2 - Venda a Prazo 30 dias - desconto de 5%
3 - Venda a Prazo 60 dias - mesmo preço
4 - Venda a Prazo 90 dias - acréscimo de 5%
5 - Venda com cartão de débito - desconto de 8%
6 - Venda com cartão de crédito - desconto de 7%'''

# entrada
venda = float(input('Informe o valor da venda: R$'));
pagamento = input('Informe a forma de pagamento:');


# processamento
if pagamento == 'Venda a vista':
    desconto = venda * 10 / 100
    valorfinal = venda - desconto
    resposta = f'O valor da venda é de {valorfinal}, pois ganhou 10% de desconto'
else:
    if pagamento == 'Venda a prazo 30 dias':
        desconto = venda * 5 / 100
        valorfinal = venda - desconto
        resposta = f'O valor da venda é de {valorfinal}, pois ganhou 5% de desconto'
    else:
        if pagamento == 'Venda a prazo 60 dias':
            resposta = 'O valor da venda continua o mesmo'
        else:
                if pagamento == 'Venda a prazo 90 dias':
                     acrescimo = venda * 5 / 100
                     valorfinal = venda + acrescimo
                     resposta = f'O valor da venda é de {valorfinal}, pois recebeu 5% de acréscimo'
                else:
                         if pagamento == 'Venda com cartão de débito':
                             desconto = venda * 8 / 100
                             valorfinal = venda - desconto
                             resposta = f'O valor da venda é de {valorfinal}, pois recebeu 8% de desconto'
                        else:
                            if pagamento == 'Venda com cartão de crédito':
                                desconto = venda * 7 / 100
                                valorfinal = venda - desconto
                                resposta = f'O valor da venda é de {valorfinal}, pois recebeu 7% de desconto'
                                     

        
        

                

# saída
print (resposta);


