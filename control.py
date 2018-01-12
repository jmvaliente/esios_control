#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################################################################################################
# Consulta en la api de la red electrica española el precio de la electricidad de cada hora del dia actual
# avisando cuales son las horas con precio por debajo de la media, por encima y la hora mas barata y cara.
# Existe la posibilidad de usar interuptores wifi para el encendido y apagado de diferentes elementos electricos
# según el precio.
# By Jose Miguel Valiente -2017-
###########################################################################################################

import requests
import json
import time
#import RPi.gpio # librería GPIO para Raspberry Pi para comunicacion entrada/salida   

co2_ce=0.65 #CO2 KW hora
co2_cd=0.16 #CO2 Kilometro diesel

hora_int=int(time.strftime('%H'))  #Capturamos la hora del sistema y refundimos el valor de str a int
precio_float=list(range(0,24)) #matriz para almacenar el Precio
i=0 #Variables contador
hora=0 #Eliminar la variable si se usa la obtenida por la api
  
    

cookies = {
    }

headers = {
    'Accept': 'application/json; application/vnd.esios-api-v1+json',
    'Content-Type': 'application/json',
    'Host': 'api.esios.ree.es',
    'Authorization': 'Token token="AÑADIR TOKEN"',
    }

datos=requests.get('https://api.esios.ree.es/indicators/1013?date='+time.strftime("%y-%m-%d"), headers=headers, cookies=cookies)#Recogida de datos
rj=datos.json() #Paso de datos a Json
print("El precio de la electricidad para el dia:",time.strftime("%y-%m-%d"))
print("Hora del dia | Precio Kw/h")
for key in rj["indicator"]["values"]:
    print(hora,"|",key["value"]/1000) # sustituir la variable "hora" por "key["datetime"]" para mostrar la hora desde la api.
    precio_float[i]=round(key["value"]/1000,4) #Capturamos valor y transformamos a Float
    i=i+1
    hora=hora+1

def media():
    precio_med=round(sum(precio_float)/24,4)
    return precio_med

def porcentaje():
    porcent=round(((precio_float[hora_int]*100)/media())-100,2)
    return porcent
  


print("Son las:",time.strftime('%H:%M'),"y el precio es de",precio_float[hora_int],"€/kWh")
print("El precio  maximo es de:",max(precio_float))
print("El precio minimo es de:",min(precio_float))
print("La diferencia sobre el precio medio es:",porcentaje(),"%")
print("El precio medio es: ",media())

if precio_float[hora_int+1]>media(): #control por precio para desnexion de algun elemento electrico. Eliminar if si no se va a usar.   
    print("Desconexión termo") # ejemplo de desconexion del un termo.
    #Codigo abrir o cerrar un rele/interruptor
    print("Ahorro aproximado segun un calentador de agua de 2200W encendido 30 min:",round((max(precio_float)/2)*2.2,2),"euros diarios y",round(((max(precio_float)/2)*2.2)*365,2),"euros al año")
    print("no solo ahorras si no que no estas emitiendo",round((co2_ce/2)*2.2,2),"Kg de CO2 diario, que equivale a",round((co2_ce/2)*2.2/co2_cd,2),"Kms de un coche diesel diario, o",round(((co2_ce/2)*2.2/co2_cd)*365,2),"Kms anuales")

if precio_float[hora_int+1]<media(): #control por precio para conexion de algun elemento electrico. Eliminar if si no se va a usar.   
    print("Conexión termo") # ejemplo de desconexion del un termo.
    #Codigo abrir o cerrar un rele/interruptor
