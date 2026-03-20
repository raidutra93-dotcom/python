

b = input("digite uma anotação:")
with open('diario.txt','a',encoding='utf-8') as diario:
    from datetime import datetime
    agora = datetime.now().strftime('%d/%m/%Y %H:%M')
    diario.write(agora)
    diario.write(b)
  
  
