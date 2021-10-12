import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont, ImageTk

from datetime import datetime


def ui():
    #das normale bild erzeugen (modus L = 8 bit greyscale) color = 128 => grau
    normalimg = Image.new('L', (720, 576), color=128)
    
    #Font und größe einstellen
    d = ImageDraw.Draw(normalimg)
    fnt = ImageFont.truetype("arial.ttf", 55)

    #Mit weißem text "NWTK ist klasse!" auf das bild schreiben
    d.text((normalimg.width/2-200, normalimg.height/2), "NWTK ist klasse!", font= fnt, fill=255)
    
    #Das zufallsarray generieren (werte zwischen 0 und 255 | schwarz - graustufen - weiß) und die 3 möglichen bilder erzeugen
    noisearray = np.random.randint(0,255,size=(720, 576))

    xorimg = Image.new('L', (720, 576), color=0)
    orimg = Image.new('L', (720, 576), color=0)
    andimg = Image.new('L', (720, 576), color=0)


    #für jeden pixel die 3 operationen durchgehen und in das richtige bild speichern
    t = datetime.now()
    for x in range(normalimg.width):
        for y in range(normalimg.height):
            col = normalimg.getpixel((x,y)) ^ noisearray[x][y]
            xorimg.putpixel((x,y),col.item())
            col = normalimg.getpixel((x,y)) | noisearray[x][y]
            orimg.putpixel((x,y),col.item())
            col = normalimg.getpixel((x,y)) & noisearray[x][y]
            andimg.putpixel((x,y),col.item())
    tt = datetime.now()
    print("Calc time: {}".format(tt-t))


    #UI aufsetzten und tabs mit bilder in labels erstellen
    root = tk.Tk()
    root.title("Bitwise image-operations")

    tabControl = ttk.Notebook(root)

    tab0 = ttk.Frame(tabControl)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.add(tab0, text="Normal")
    tabControl.add(tab1, text="XOR")
    tabControl.add(tab2, text="OR")
    tabControl.add(tab3, text="AND")

    tabControl.pack(expand=1, fill="both")

    #Muss gemacht werden so dass die bilder angezeigt werden
    photonorm = ImageTk.PhotoImage(normalimg)
    photoxor = ImageTk.PhotoImage(xorimg)
    photoor = ImageTk.PhotoImage(orimg)
    photoand = ImageTk.PhotoImage(andimg)


    ttk.Label(tab0, image=photonorm).grid(column=0,row=0,padx=60,pady=30)
    ttk.Label(tab1, image=photoxor).grid(column=0,row=0,padx=50,pady=30)
    ttk.Label(tab2, image=photoor).grid(column=0,row=0,padx=40,pady=30)
    ttk.Label(tab3, image=photoand).grid(column=0,row=0,padx=30,pady=30)

    root.mainloop()

ui()
