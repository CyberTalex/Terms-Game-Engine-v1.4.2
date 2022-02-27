from tkinter import Tk
from tkinter import filedialog
import tkinter as tk
import sys
import os
import json
from PyQt5.QtWidgets import QWidget,QMainWindow,QTextEdit,QVBoxLayout,QApplication,QAction,QFileDialog,QInputDialog
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import pygame
from pygame.locals import *
from constants import *
import main
#from MeshRenderer import CubeMesh, ChairMesh

pencere=tk.Tk()
pencere.title("Terms Game Engine v1.4.2")
pencere.geometry("400x100")

def dosyaYap():
    dosya = open("Kayıtlı_Kod_Dosyası.py", "w")
    
dugme = tk.Button(text = "Yeni Proje", command=dosyaYap())
dugme.pack()

pencere.mainloop()

def openFile():
    options=QFileDialog.Options()
    data=QFileDialog.getOpenFileName(widget,"Dosya Seç","","All Files(*)",options=options)
    fileopen=open(data[0],"r")
    textbox.setPlainText(fileopen.read())
    fileopen.close()


def saveactionFun():
    options=QFileDialog.Options()
    data=QFileDialog.getSaveFileName(widget,"Dosya Kaydet","",options=options)
    fileopen=open(data[0],"w")
    fileopen.write(textbox.toPlainText())
    fileopen.close()

def initNotePad():
    if os.path.exists("./config.json"):
        data=open("./config.json","r")
        dictdata=json.loads(data.read())
        data.close()
        return dictdata
    else:
        openfile=open("./config.json","w")
        dictdata={"size":15}
        openfile.write(json.dumps(dictdata))
        openfile.close()
        return dictdata

def fontActionFun():
    data=QInputDialog.getInt(widget,"Yazı Boyutu","Yazı Boyutu",initData['size'],12,48,1)
    if data[1]:
        initData['size']=data[0]
        openfile=open("./config.json","w")
        openfile.write(json.dumps(initData))
        openfile.close()

        textdata=textbox.toPlainText()
        textbox.setPlainText("")
        textbox.setFontPointSize(data[0])
        textbox.setPlainText(textdata)




app=QApplication(sys.argv)

mainwindow=QMainWindow()
mainwindow.setWindowTitle("Kod Editörü")
widget=QWidget()

#menu
menubar=mainwindow.menuBar()
filemenu=menubar.addMenu("Dosya")
openaction=QAction("Aç")
openaction.triggered.connect(openFile)
filemenu.addAction(openaction)

saveaction=QAction("Kaydet")
saveaction.triggered.connect(saveactionFun)
filemenu.addAction(saveaction)

setting=menubar.addMenu("Ayarlar")
fontaction=QAction("Yazı Boyutu")
fontaction.triggered.connect(fontActionFun)
setting.addAction(fontaction)


layout=QVBoxLayout()
layout.setContentsMargins(0,0,0,0)

textbox=QTextEdit()

initData=initNotePad()


textbox.setFontPointSize(initData['size'])
layout.addWidget(textbox)
widget.setLayout(layout)

mainwindow.setCentralWidget(widget)

mainwindow.show()
mainwindow.showMaximized()

sys.exit(app.exec_())