'''Elabore um algoritmo para testar se uma senha digita é igual a “batatafrita”.
Se a senha estiver correta escreva “Acesso permitido”, do contrário emita
a mensagem “Você não tem acesso ao sistema”.'''

#entrada
senha = input('Digite a senha:');

#processamento
if senha == 'batatafrita':
    resposta = 'Acesso permitido.'
else:
    resposta = 'Você não tem acesso ao sistema.'

# saída
print(resposta);
