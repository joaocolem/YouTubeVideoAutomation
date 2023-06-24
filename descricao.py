
def descricao(data):
    with open("ArquivosAuxiliares\descricao_body.txt",'r',encoding="utf-8") as arquivo:
        descricao_body = arquivo.read()
    with open("ArquivosAuxiliares\\tempo.txt",'r', encoding= 'unicode_escape') as arquivo1:
        tempo = arquivo1.read()
    descricao = "Horóscopo do dia: " + data +"\n\n"+descricao_body + tempo
    with open("ArquivosAuxiliares\descricao.txt",'w',encoding="utf-8") as arquivo2:
        arquivo2.write(descricao)