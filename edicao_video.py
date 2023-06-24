import random
from time import strftime
from time import gmtime

from moviepy.editor import *

def edicao_video(datadodia):
    signos = ['aries', 'touro','gemeos','cancer','leao','virgem','libra','escorpiao','sagitario','capricornio','aquario','peixes']


    def clip_signo(i):

        signos = ['aries', 'touro', 'gemeos', 'cancer', 'leao', 'virgem', 'libra', 'escorpiao', 'sagitario', 'capricornio','aquario', 'peixes']

        audio = AudioFileClip("Audios\\"+signos[i]+".wav")
        duration = audio.duration

        n_frase = random.randint(0,70)

        audio2 = AudioFileClip("ArquivosAuxiliares\\audiofrases\\"+str(n_frase)+".wav")
        duration2 = audio2.duration


        imgc = (ImageClip("ArquivosAuxiliares\\imagensfrases\\"+str(n_frase)+".jpg")
                .set_duration(duration2)
                .resize(height=500)
                .margin(right=20, top=30, opacity=0)
                .set_position((90,160)))

        durationx = duration2+duration
        clip_signo = VideoFileClip("ArquivosAuxiliares\\vsignos\\"+signos[i]+".m4v").subclip(0,19)
        clip_signo = clip_signo.loop(duration=duration)

        clip_frase = VideoFileClip("ArquivosAuxiliares\\vsignos\\"+signos[i]+".m4v").subclip(21,39)
        clip_frase = clip_frase.loop(duration=duration2)

        video_frase = CompositeVideoClip([clip_frase,imgc])

        video = CompositeVideoClip([clip_signo,video_frase.set_start(duration)])
        audio = concatenate_audioclips([audio,audio2])
        video.audio = CompositeAudioClip([audio])

        return(video,durationx)

    videos_signos = []

    audio_intro = AudioFileClip("Audios\intro.wav")
    audio_intro_duration = audio_intro.duration

    video_intro_back = VideoFileClip("ArquivosAuxiliares\\intro.m4v").subclip(0,audio_intro_duration)
    video_intro = CompositeVideoClip([video_intro_back])
    video_intro.audio = CompositeAudioClip([audio_intro])
    videos_signos.append(video_intro)
    marcacao = []
    marcacao.append(audio_intro_duration)

    for i in range(len(signos)):
        video_s= clip_signo(i)
        video = video_s[0]
        videos_signos.append(video)
        marcacao.append(video_s[1])
    video = concatenate_videoclips(videos_signos,method="chain")
    duration = video.duration

    signos_simbolo = ['Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem', 'Libra', 'Escorpião', 'Sagitário','Capricórnio', 'Aquário', 'Peixes','FIM']
    txt_clip = TextClip(datadodia, fontsize=40, color='white',font='Xolonium-Bold')
    txt_clip = txt_clip.set_pos('top','right').set_start(50).set_duration(duration-50)

    musica = AudioFileClip("ArquivosAuxiliares\musica.mp3").subclip(0,duration).fx(afx.volumex, 0.4)
    video = CompositeVideoClip([video,txt_clip])
    video.audio = CompositeAudioClip([video.audio,musica])

    video.write_videofile("video\horoscopo_do_dia.mp4",fps=20,threads=16,logger=None,codec="mpeg4",preset="slow",ffmpeg_params=['-b:v','10000k'])
    pontos=[]
    tempo_signos =""
    for i in range(len(marcacao)-1):
        if i==0:
            pontos.append(marcacao[i])
        else:
            pontos.append(marcacao[i]+pontos[i-1])
        tempo = pontos[i]
        tempo = strftime("%H:%M:%S", gmtime(tempo))
        tempo_signos = (tempo_signos+"\n"+tempo+"  -  " + signos_simbolo[i])
    with open("ArquivosAuxiliares\\tempo.txt", "w") as arquivo:
        arquivo.write(tempo_signos)
