import tkinter as tk
import ctypes
import random
import os
from PIL import Image, ImageTk
from functools import partial
import math
import tkinter.filedialog as fd

img_Tmb = []
root = tk.Tk()
Wallpapers = list(filter(lambda x: x.endswith('.jpg'), os.listdir()))
Walpr_len = len(Wallpapers)-1
print(Wallpapers)
print(Walpr_len)

def CreateTumd():
    if 'Tumbnail' in os.listdir():
        Wallpapers = list(filter(lambda x: x.endswith('.jpg'), os.listdir()))
        Walpr_len = len(Wallpapers)-1
        for k in range(Walpr_len+1):
            img = Image.open(Wallpapers[k])
            img.thumbnail(size=(150, 150))
            img.save(os.getcwd() + '\\Tumbnail\\' + Wallpapers[k])
    else:
        os.mkdir('Tumbnail')
        return;

def CreateList():
    Wallpapers = list(filter(lambda x: x.endswith('.jpg'), os.listdir()))
    Walpr_len = len(Wallpapers)-1
    n = 0
    for i in range(Walpr_len- math.ceil(Walpr_len/2)):
        for j in range(2):
            frm_item = tk.Frame(
                master=frm_list,
                relief=tk.RAISED,
                borderwidth=1
            )
            img_in = Image.open(os.getcwd() + '\\Tumbnail\\' + Wallpapers[n])
            img_Tmb.append(ImageTk.PhotoImage(img_in))

            frm_item.grid(row=i, column=j, padx=5, pady=5)
            btn_BG =tk.Button(master=frm_item, image=img_Tmb[n], command= partial(changeBG, Wallpapers[n]))
            btn_BG.pack()

            btn_del = tk.Button(master=frm_item, text='удалить', command= partial(deleteBG, Wallpapers[n]))
            btn_del.pack()

            btn_shct = tk.Button(master=frm_item, text='Ярлык', command=createShotcutBG)
            btn_shct.pack()
            n = n + 1
    if Walpr_len+1 % 2 != 0:
        frm_item = tk.Frame(
            master=frm_list,
            relief=tk.RAISED,
            borderwidth=1
        )
        img_in = Image.open(os.getcwd() + '\\Tumbnail\\' + Wallpapers[Walpr_len])
        img_Tmb.append(ImageTk.PhotoImage(img_in))

        frm_item.grid(row=Walpr_len- math.ceil(Walpr_len/2), column=0, padx=5, pady=5)
        btn_item = tk.Button(master=frm_item, image=img_Tmb[Walpr_len], command=partial(changeBG, Wallpapers[Walpr_len]))
        btn_item.pack()

        btn_del = tk.Button(master=frm_item, text='удалить', command=partial(deleteBG, Wallpapers[Walpr_len]))
        btn_del.pack()

def changeBG(BGname):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+'\\'+ BGname, 3)
    return;

def deleteBG(BGname):
    os.remove(BGname)
    os.remove(os.getcwd() + '\\Tumbnail\\' + BGname)

    Wallpapers = list(filter(lambda x: x.endswith('.jpg'), os.listdir()))
    Walpr_len = len(Wallpapers)-1

    CreateTumd()
    CreateList()

def createShotcutBG(BGname):
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")

def SetRandomWallpaper():
    changeBG(Wallpapers[random.randint(0,4)])

#--------------------------------------------------------------------------------------------------------------------
root['bg'] = '#aaaaaa'
root.title("Обои")
root.iconphoto(True, tk.PhotoImage(file='icon.png'))
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)
root.resizable(width=False, height=False)

frm_panel = tk.Frame(root)
frm_panel.grid(row=0, column=0, sticky="ns")

btn_rand = tk.Button(master=frm_panel, text='случайные обои', command= SetRandomWallpaper,relief=tk.RAISED,)
btn_rand.grid(row=1, column=0, sticky="ew", padx=5)


frm_panel.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frm_list= tk.Frame(root)

CreateTumd()
CreateList()


frm_list.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

root.mainloop()