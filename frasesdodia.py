from PIL import Image, ImageFont, ImageDraw
def troca(i):
    img = Image.open("ArquivosAuxiliares\imagensfrases\\"+str(i)+".jpg")
    width, height = img.width, img.height

    draw = ImageDraw.Draw(img)
    caminho_fonte = r"C:\Windows\Fonts\Impact.TTF"
    font = ImageFont.truetype(caminho_fonte, 20)
    x, y = (width - 200, height-40)
    text = " Canal Horóscopo diário "
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill='black')
    draw.text((x, y), text, fill=('white'), font=font)
    img.save('ArquivosAuxiliares\imagensfrases\\'+str(i)+".jpg")

for i in range(71):
    troca(i)
