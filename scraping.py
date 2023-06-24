import random
import requests
from bs4 import BeautifulSoup


def joaobidu(signo):
    response = requests.get('https://joaobidu.com.br/horoscopo/signos/previsao-'+signo+'/amanha/')
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    leitura_amanha = site.find('div', attrs={'class': 'zoxrel left'})
    horoscopo_dia=leitura_amanha.text
    horoscopo_dia= horoscopo_dia.split("\n", maxsplit=8)
    horoscopo_dia.pop()
    for i in range(5):
        horoscopo_dia.pop(1)
    horoscopo_dia=" ".join(horoscopo_dia)
    dia = ['DOM','SEG','TER','QUA','QUI','SEX','SAB']
    for i in range(len(dia)):
        horoscopo_dia=horoscopo_dia.replace(dia[i],"")
    horoscopo_dia = horoscopo_dia.replace("love", "lóve")
    horoscopo_dia = horoscopo_dia.replace(".Hoje, ", ". Hoje")
    return(horoscopo_dia)
def virtual(signo):
    response = requests.get('https://www.horoscopovirtual.com.br/horoscopo/'+signo+'/amanha')
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    leitura_amanha = site.find('p', attrs={'class': 'text-pred'})
    horoscopo_dia=leitura_amanha.text
    horoscopo_dia= horoscopo_dia.split("\n")
    horoscopo_dia.pop()

    horoscopo_dia=" ".join(horoscopo_dia)
    horoscopo_dia=horoscopo_dia.replace("QUA","")
    horoscopo_dia = horoscopo_dia.replace("love", "lóve")
    horoscopo_dia = horoscopo_dia.replace("Compartilhar", "")
    horoscopo_dia = horoscopo_dia.replace(".Hoje, ", ". Hoje")
    return(horoscopo_dia)
def astrologyk(signo,signos):
    response = requests.get('https://pt.astrologyk.com/horoscopo/amanha/'+signo)
    content = response.content
    site = BeautifulSoup(content, 'html.parser')

    leitura_amanha = site.find('div', attrs={'class': 'col-12'})
    horoscopo_dia = leitura_amanha.text
    horoscopo_dia = horoscopo_dia.split("•",maxsplit=1)
    horoscopo_dia.pop()

    horoscopo_dia = " ".join(horoscopo_dia)

    horoscopo_dia = horoscopo_dia.replace("love", "lóve")
    horoscopo_dia = horoscopo_dia.replace("Compartilhar", "")
    horoscopo_dia = horoscopo_dia.replace("Horóscopo de amanhã: "+signos, "")
    horoscopo_dia = horoscopo_dia.replace(".Hoje, ", ". Hoje")
    return(horoscopo_dia)

def horoscopo():

    horoscopo = []
    with open("ArquivosAuxiliares\marcia.txt","r", encoding="utf-8") as arquivo:
        intro = arquivo.readlines()
    aleat = random.randint(0,2)
    horoscopo.append(intro[aleat])

    introx =  " ".join(horoscopo)
    with open("TextosSignos\intro.txt", "w") as arquivo:
        arquivo.write(introx)
    horoscopo = []
    signos = ['aries', 'touro','gemeos','cancer','leao','virgem','libra','escorpiao','sagitario','capricornio','aquario','peixes']
    signos_acento = ['Áries', 'Touro','Gêmeos','Câncer','Leão','Virgem','Libra','Escorpião','Sagitário','Capricórnio','Aquário','Peixes']
    for i in range(len(signos)):
        horoscopo.append(signos_acento[i]+"!")
        horoscopo.append(astrologyk(signos[i], signos_acento[i]) +" ")
        horoscopo.append(virtual(signos[i]) + " ")
        horoscopo.append(joaobidu(signos[i]))
        horoscopox = " ".join(horoscopo)
        nome_arquivo = signos[i]+".txt"
        with open("TextosSignos\\"+nome_arquivo,"w") as arquivo:
            arquivo.write(horoscopox)
        horoscopo=[]
