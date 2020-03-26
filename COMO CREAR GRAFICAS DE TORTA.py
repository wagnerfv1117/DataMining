#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:06:37 2020

@author: wagner
"""
import matplotlib.pyplot as plt

impr = ["ENERO", "FEBRERO", "MARZO", "ABRIL"]
vol = [25, 25, 25, 25]
expl =(0, 0.05, 0, 0)
plt.pie(vol, explode=expl, labels=impr, autopct='%1.1f%%', shadow=True)
plt.title("CONSUMO DE SERVICIOS PUBLICOS", bbox={"facecolor":"0.8", "pad":5})
plt.legend()