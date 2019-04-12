import random
import sys
import time

def galoevar(x,y,z):
  muerte = 0
  for i in xrange(x):
    galo = 0
    evari = 0
    suma = 0
    galo = galo+random.random()
    evari = evari+random.random()
    galo = galo*y
    evari = evari*y
    suma = galo - evari
    if abs(suma)<=z:
      muerte = muerte+1
      
  print ("el numero de muertes fue:")
  print (muerte)
  print ("la probabilidad de muerte es de :")
  x = x +0.0
  print (float(muerte/x))
simulaciones = int(raw_input('Ingrese el numero de simulaciones:'))
frantiem = int(raw_input('Ingrese franja de tiempo del duelo en minutos:'))
franespe = float(raw_input('Ingrese tiempo de espera para el duelo en minutos:'))
galoevar(simulaciones,frantiem,franespe)
