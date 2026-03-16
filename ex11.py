aluno = {
    'nome': 'Maria',
    'telefone': 32999723714,
    'email': 'raidutra93@gmail.com ',
    'cidade':'Rio Pomba'
}
print(aluno.items())
aluno['instagran'] = 'aasdadad'
print(aluno.items())
del aluno['telefone']
print(aluno.items())
if 'email' in aluno:
    print('Chave existe!')
