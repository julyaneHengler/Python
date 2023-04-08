'''Elabore um algoritmo para testar se uma senha digitada é igual a “MinhaSenha”.
Se a senha estiver correta escreva “Acesso permitido”,do contrário emita a mensagem
“Você não tem acesso ao sistema”.'''

# entrada
senha = input('Digite a senha:');

# processamento
if senha == 'MinhaSenha':
    resposta = ('Acesso Permitido');
else:
    resposta = ('Você não tem acesso ao sistema');

# saida
print(resposta);
