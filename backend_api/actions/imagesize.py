from PIL import Image
import os

WIDTH = 650
HEIGHT = 520

def imagesize(imgurl,cutcount,tcut = 0):
    imgdir,basename = os.path.split(imgurl)
    savedir = os.path.join(imgdir,'thumbs')
    savepath = os.path.join(savedir,basename)

    if not os.path.exists(savedir):
        os.mkdir(savedir)

    newy = round(HEIGHT - (1.25+(0.25*cutcount)+(0.5*tcut)+0.416+0.425)*96 + 0.5*96)
    img = Image.open(imgurl)
    x,y = img.size
    newx = round(newy * x / y)
    if newx >= WIDTH:
        newx = WIDTH-50 
    img.thumbnail(size = (newx,newy))
    img.save(savepath)

    return savepath
