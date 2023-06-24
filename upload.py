import thumbnail
import os
import pickle
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request

# Defina as credenciais e escopos necessários para a autenticação
CLIENT_SECRETS_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

with open("ArquivosAuxiliares\descricao.txt", "r", encoding='utf-8') as arquivo:
    descricao = arquivo.read()
with open("ArquivosAuxiliares\\tempo.txt", "r", encoding='unicode_escape') as arquivo1:
    tempo = arquivo1.read()

data=thumbnail.thumbnail()

# Autenticar a aplicação
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=SCOPES,
            redirect_uri='urn:ietf:wg:oauth:2.0:oob'
        )
        auth_url, _ = flow.authorization_url(prompt='consent')
        print('Por favor, visite esta URL e depois coloque o código aqui: {}'.format(auth_url))
        code = input('Código: ')
        flow.fetch_token(code=code)
        creds = flow.credentials
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

# Fazer o upload do vídeo com a thumbnail
youtube = build(API_SERVICE_NAME, API_VERSION, credentials=creds)
request_body = {
    'snippet': {
        'title': "Horóscopo do dia! - " + data,
        'description': descricao,
        'tags': ['horóscopo 2023',
'signos 2023',
'previsões 2023',
'signo leao',
'signo de Áries',
'signo touro',
'signo escorpiao',
'signo sagitario',
'horóscopo do dia',
'horóscopo do dia de hoje',
'horóscopo de hoje',
'horóscopo diário',
'parar para todos os signos',
'thiago giatho médio',
'relacionamento',
'astrologia',
'marcia fernandes',
'marcia sensitiva',
'previsão',
'signos',
'todos os signos',
'signo2023',
'2023',
'amanhã',
'horóscopo de amanhã',],
        'categoryId': '22',
    },
    'status': {
        'privacyStatus': 'public' # Opções: public, private ou unlisted
    }
}
media = MediaFileUpload('video/horoscopo_do_dia.mp4', chunksize=1024*1024, resumable=True)
#media = MediaFileUpload('video-output.mp4', chunksize=1024*1024, resumable=True)



def up():
    try:
        response_upload = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=media
        ).execute()

        youtube.thumbnails().set(
            videoId=response_upload.get('id'),
            media_body=MediaFileUpload('video/thumbnail.png')
        ).execute()

        print('Vídeo enviado com sucesso! URL do vídeo:', 'https://www.youtube.com/watch?v=' + response_upload['id'])
    except HttpError as e:
        print('Ocorreu um erro:', e)

