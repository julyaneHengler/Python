'''Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o
semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado
(media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9).'''

# entrada
aluno = input('Informe o nome do aluno:');
nota1 = float(input('Digite a primeira nota do aluno:'));
nota2 = float(input('Digite a segunda nota do aluno:'));
nota3 = gloat(input('Digite a terceira nota do aluno:'));

# processamento
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    resposta = ('O aluno',aluno,'foi aprovado!')
else:
    if media <= 5:
        resposta = ('O aluno',aluno,' foi reprovado!')
        
else
    if media > 5 < 7:
        resposta = ('O aluno', aluno, ' está de recuperação!')

# saída
print(resposta);

