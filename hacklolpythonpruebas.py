# -*- coding: utf-8 -*-
"""

Spyder Editor

This is a temporary script file.
client.devices()
"""
#import time
from ppadb.client import Client
from PIL import Image
import re 
import pytesseract
import cv2
import time
import random
client = Client(host="127.0.0.1", port=5037)
devices = client.devices()
device_0=devices[0]
#resoluticon 1600 * 900

# campeones
campeones_yordles = ("Poppy","Gnar","Lulu","Vex","Corki","Vex","Zig")
campeones_inovadores= ("Ekko","Ezreal","Jayce","Zilean","Seraphine","Singed")
tiempo: float = 1.2
seleccion= campeones_yordles
#

def mirar_cartas ():
    campeones=""
    capturar_imagen()
    for cont in range (5):
        aumento_x=273
        image=Image.open("base.png")
        image_campeon=image.crop((215+(aumento_x*cont),290,392+(aumento_x*cont),330))    
        image_campeon.save("campeon.png")
        imagen2= cv2.imread("campeon.png")
        gray_campeon = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
        pytesseract.pytesseract.tesseract_cmd= r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
        image_campeon_gray : str =pytesseract.image_to_string(gray_campeon)      
        campeones=campeones+image_campeon_gray
        for i in seleccion:      
            if(i in image_campeon_gray):
                print("Compre a:" + image_campeon_gray)
                if cont==0:
                    device_0.shell("input touchscreen swipe 337 168 0 0 1")
                elif cont==1:
                    device_0.shell("input touchscreen swipe 652 168 0 0 1")
                elif cont==2:
                    device_0.shell("input touchscreen swipe 892 168 0 0 1")
                elif cont==3:
                    device_0.shell("input touchscreen swipe 1173 168 0 0 1")
                elif cont==4:
                    device_0.shell("input touchscreen swipe 1438 168 0 0 1")
        print(campeones)
                    
def vender_campeones():
    #arrastrar
    
    device_0.shell("input touchscreen tap 290 778")
    for cont2 in range(9):
        #305 430 aumentos 120
        x= "input touchscreen tap "+str(305+(125*cont2))+" 804"
        time.sleep(0.3)
        device_0.shell(x)
        time.sleep(0.3)
        #device_0.shell("input touchscreen swipe 305 804 1502 801 1000")            
        esta=0
        for campeon in seleccion:
            if traducir_imagen(1370,14,1512,47) in campeon:
                esta=1
        if esta==1:
            device_0.shell("input touchscreen swipe "+str(305+(125*cont2))+" 804 1535 808 100")                
 

def juego():
    capturar_imagen()    
    gold =traducir_imagen(1480,776,1555,830)
    list_of_numers= re.findall(r'\d+', gold)
    result_number = ''.join(list_of_numers)
    print("Hay: " + str(result_number) +" de oro" +gold)
    try:
        oro:int= int(gold)
    except:
        oro=0
        #print("error oro")

    if(oro>30):
        device_0.shell("input touchscreen swipe 1495 595 5 5 3")
        #print("soy happy")
  

def capturar_imagen():
    image= device_0.screencap()
    with open("base.png","wb") as f:
        f.write(image)
        
def jugar(tiempo):
    capturar_imagen()
    image=Image.open("base.png")
    image_jugar=image.crop((1273,784,1421,830)) 
    image_jugar.save("jugar.png")
    imagen_jugar= cv2.imread("jugar.png")
    gray_jugar = cv2.cvtColor(imagen_jugar, cv2.COLOR_BGR2GRAY)
    pytesseract.pytesseract.tesseract_cmd= r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    texto_imagen_jugar : str =pytesseract.image_to_string(gray_jugar)      
    #print(texto_imagen_jugar)
    if ("JUGAR" in texto_imagen_jugar):
        print("ha")
        #jugar
        device_0.shell("input touchscreen swipe 1276 789 0 0 1")
        #normal
        device_0.shell("input touchscreen swipe 233 507 0 0 1")
        time.sleep(tiempo)
        #normal
        device_0.shell("input touchscreen swipe 1261 811 0 0 1")
        time.sleep(tiempo)
        #buscar partida
        device_0.shell("input touchscreen swipe 731 662 0 0 1")
        time.sleep(tiempo)
              
def aceptar_partida():
    capturar_imagen()
    image=Image.open("base.png")
    image_aceptar=image.crop((690,645,916,705)) 
    image_aceptar.save("aceptar.png")
    imagen_aceptar= cv2.imread("aceptar.png")
    gray_aceptar = cv2.cvtColor(imagen_aceptar, cv2.COLOR_BGR2GRAY)
    pytesseract.pytesseract.tesseract_cmd= r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    texto_imagen_aceptar : str =pytesseract.image_to_string(gray_aceptar)  
    #print(texto_imagen_aceptar)
    if ("ACEPTAR" in texto_imagen_aceptar):
         #aceptar partida
         device_0.shell("input touchscreen swipe 802 687 0 0 1")
         time.sleep(tiempo)
         return ("juego")
    else:
        return("buscando")

def traducir_imagen(x0,y0,x1,y1):
    capturar_imagen()
    image=Image.open("base.png")
    image_recortada=image.crop((x0,y0,x1,y1)) 
    image_recortada.save("recorte.png")
    imagen_recortada_cv= cv2.imread("recorte.png")
    gray_imagen_recortada = cv2.cvtColor(imagen_recortada_cv, cv2.COLOR_BGR2GRAY)
    pytesseract.pytesseract.tesseract_cmd= r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    texto_recortado : str =pytesseract.image_to_string(gray_imagen_recortada)
    return texto_recortado
    print(texto_recortado)


while 1==1:
    if ("rechazado" in traducir_imagen(530,274,1066,614)):
        device_0.shell("input touchscreen swipe 884 572 0 0 1")
    
    jugar(tiempo)
    prueba= aceptar_partida()
    jugando=1
    juego()   
    vender_campeones()
    mirar_cartas()
    print(traducir_imagen(0, 0, 1600, 900))


#error
