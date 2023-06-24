import time

import descricao
import scraping, audiosSignos,thumbnail,edicao_video, Convert
import upload

#scraping.horoscopo()
print("Scrap ok")
#audiosSignos.TextToSpeech.folder('TextosSignos')
print("Audios ok")
#data = thumbnail.thumbnail()
print("Thumbnail ok")
#edicao_video.edicao_video(data)
print("Edicao ok")
#descricao.descricao(data)
print("Descrição ok")
Convert.convert()
print("Conversão ok")
time.sleep(60)
#upload.up()
print("Upload ok")


