t={
    'Raí':[10,10,10],
    'Marcos':[10,10,10],
    'Pedrin':[10,10,10],
    'Maria':[10,10,10],
}
for aluno, notas in t.items():
    media = sum(notas) / len(notas)
    situacao = "Aprovado" if media >= 6.0 else "Reprovado"
    
    print(f"{aluno} – Média: {media:.1f} – Situação: {situacao}")