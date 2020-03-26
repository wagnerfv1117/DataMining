#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:15:36 2020

@author: wagner
"""


import pandas as pd#se importa la librería respectiva, para pulir los datos
import matplotlib.pyplot as plt#se importa la respectiva librería, para graficar esos datos del csv


datos=pd.read_csv('download.csv')#se importan los datos, los cuales deben estar dentro de la misma carpeta, donde está el algoritmo.
df=pd.DataFrame(datos)#se procede a crear el dataframe con base a esos datos dispersos en el CSV

df.groupby('Fecha')['Valor'].sum().plot(kind='barh',legend='Reverse')# se procede a realizar un agrupamiento de los datos que quiero solicitar, y verificar
plt.xlabel('')#se procede a seleccionar el tipo de grafica, para visualizar los datos.

#df.Valor.groupby(df.Valor).sum