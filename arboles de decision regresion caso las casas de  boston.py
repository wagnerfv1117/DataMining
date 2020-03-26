#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:48:04 2020

@author: wagner
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


boston = datasets.load_boston()
print(boston)
print()

print ('informacion del dataset')
print(boston.keys())
print()

print('caracteristicas del dataset:')
print(boston.DESCR)
print('cantidad de datos:')
print(boston.data.shape)
print()


X_adr = boston.data [:, np.newaxis, 5]

y_adr = boston.target

plt.scatter(X_adr, y_adr)
plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_adr,y_adr)

from sklearn.tree import DecisionTreeRegressor

adr = DecisionTreeRegressor(max_depth = 5)


adr.fit(X_train, y_train)
Y_pred = adr.predict(X_test)

X_grid = np.arange(min(X_test),max(X_test), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter (X_test, y_test)
plt.plot(X_grid, adr.predict(X_grid), color='red', linewidth=3)
plt.show()     

print('DATOS DEL MODELO ARBOLES DE DECISION Y REGRESION')       
print()

print('precision del modelo')
print(adr.socre(X_train, y_train))

             

