from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import datetime

def thumbnail():
    coord = (455,400)
    coord1 = (55,565)
    dia = (datetime.datetime.now() + datetime.timedelta(days=1)).day
    mes = (datetime.datetime.now() + datetime.timedelta(days=1)).month
    ano = (datetime.datetime.now() + datetime.timedelta(days=1)).year

    dia_semana = dia_da_semana(ano,mes,dia)




    mes_x = ["JANEIRO", 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO','JULHO', 'AGOSTO','SETEMBRO','OUTUBRO',"NOVEMBRO",'DEZEMBRO']


    dia_mes = mes_x[mes-1]
    if mes<10:
        mes = "0"+str(mes)
    data = str(dia) +"/"+str(mes)+"/"+str(ano)
    dia_semana = str(dia_semana)+data
    imagem = Image.open(r'ArquivosAuxiliares\thumbeditavel.png')
    caminho_fonte = r"C:\Windows\Fonts\Impact.TTF"
    font = ImageFont.truetype(caminho_fonte, 150)
    font2 = ImageFont.truetype(caminho_fonte, 120)

    desenho = ImageDraw.Draw(imagem)
    desenho.text(coord, dia_mes, font=font, fill='yellow')
    desenho.text(coord1, dia_semana, font=font2, fill='red')
    imagem.save(f'video\\thumbnail.png')
    return(dia_semana)


def dia_da_semana(ano,mes,dia):
    a = datetime.date(ano,mes,dia)
    b = a.weekday()

    semana = ['SEGUNDA - ', 'TERÇA - ', 'QUARTA - ', 'QUINTA - ', 'SEXTA - ', 'SÁBADO - ', 'DOMINGO - ']
    return(semana[b])

