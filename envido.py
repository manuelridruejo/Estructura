from Clases import *
from MAIN import *
from funciones import *

def real_envido (jug1, puntos1, jug2, puntos2, puntos_tanto, puntos_al_no):
  print(jug1,'ha cantado REAL ENVIDO')
  print('\n',jug2,', que desea hacer?')
  print('1. Falta envido')
  print('2. Quiero')
  print('3. No quiero')
  opcion = int(input('\tElija:'))
  while opcion not in [1,2,3]:
    print(jug1,'ha cantado REAL ENVIDO')
    print('\n',jug2,', que desea hacer?')
    print('1. Falta envido')
    print('2. Quiero')
    print('3. No quiero')
    opcion = int(input('\tElija (recuerde las opciones son unicamente 1-2-3):'))
  if opcion == 1:                   
    puntos_al_no=puntos_tanto
    puntos1, puntos2 = falta_envido (jug2, puntos2, jug1, puntos1, puntos_al_no)
    
  elif opcion == 2:                    
    print('\n',jug2,' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto)
    
  elif opcion == 3:                
    print('\n',jug2,' ha dicho NO QUIERO.',jug1,'suma',puntos_tanto,'puntos')
    puntos1 += puntos_al_no
  
  return puntos1, puntos2

def falta_envido (jug1, puntos1, jug2, puntos2, puntos_al_no):
  puntos_tanto = contar_puntos_falta (puntos1,puntos2)
  print(jug1,'ha cantado FALTA ENVIDO!')
  print('\n',jug2,', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = int(input('\tElija:'))
  while opcion not in [1,2]:
    print(jug1,'ha cantado FALTA ENVIDO!')
    print('\n',jug2,', que desea hacer?')
    print('1. Quiero')
    print('2. No quiero')
    opcion = int(input('\tElija (recuerde, lass opciones son 1-2):'))

  if opcion == 1:                         
    print('\n',jug2,' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto)
          
  if opcion == 2:                         
    print('\n',jug2,' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
    puntos1 += puntos_al_no
  
  return puntos1, puntos2

def contar_tanto(cartas):
    tanto = 20
    n=0
    if cartas[1].palo == cartas[2].palo:
        tanto += (int(cartas[1].jerarquia_envido) + int(cartas[2].jerarquia_envido))
        tanto_12 = tanto
        n += 1
    if cartas[0].palo == cartas[1].palo:
        tanto += (int(cartas[1].jerarquia_envido) + int(cartas[0].jerarquia_envido))
        tanto_01 = tanto
        n += 1
    if cartas[0].palo == cartas[2].palo:
        tanto += (int(cartas[0].jerarquia_envido) + int(cartas[2].jerarquia_envido))
        tanto_02 = tanto
    if n == 2:
        tanto=max(tanto_01,tanto_02,tanto_12)
    if n == 0:
        tanto=(max(cartas[0].jerarquia_envido, cartas[1].jerarquia_envido, cartas[2].jerarquia_envido))
    return tanto

def contar_los_tantos (cartasjug1,cartasjug2):
    tanto1 = contar_tanto(cartasjug1)
    tanto2 = contar_tanto(cartasjug2)
    return tanto1, tanto2

def contar_puntos_falta (puntos1,puntos2):
  if puntos2 < puntos1:
    puntos_tanto = 30 - puntos1
  elif puntos2 > puntos1:
    puntos_tanto = 30 - puntos2
  else:
    puntos_tanto = 30 - puntos1
  return puntos_tanto

def sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto):
  tanto1, tanto2 = contar_los_tantos (jug1, jug2)
  if jug1 == mano:
    print('\n',jug1+':',tanto1)

    if tanto2>tanto1:
      print(jug2+':',tanto2,'son mejores puto de mierda')
      puntos2 += puntos_tanto
      print(jug2,'suma',puntos_tanto,'puntos')

    else:
      print(jug2+': son buenas')
      puntos1 += puntos_tanto
      print(jug1,'suma',puntos_tanto,'puntos')

  elif jug2 == mano:
    print('\n',jug2+':',tanto2)

    if tanto1>tanto2:
      print(jug1+':',tanto1,'son mejores.')
      puntos1 += puntos_tanto
      print(jug1,'suma',puntos_tanto,'puntos')

    else:
      print(jug1+': son buenas')
      puntos2 += puntos_tanto
      print(jug2,'suma',puntos_tanto,'puntos')

  return puntos1, puntos2
  
def envido (jug1, puntos1, jug2, puntos2):
  print('Que desea cantar?')
  print('1. Envido')
  print('2. Real envido')
  print('3. Falta envido')
  opcion = int(input('\tElija:'))
  while opcion not in [1,2,3]:
    print('Que desea cantar?')
    print('1. Envido')
    print('2. Real envido')
    print('3. Falta envido')
    opcion = int(input('\tElija (recuerde las opciones son 1-2-3):'))

  if opcion == 1:             #ENVIDO (j1)
    puntos_tanto = 2
    puntos_al_no = 1
    print(jug1,'ha cantado ENVIDO')
    print('\n',jug2,', que desea hacer?')
    print('1. Envido')
    print('2. Real envido')
    print('3. Falta envido')
    print('4. Quiero')
    print('5. No quiero')
    opcion = int(input('\tElija:'))
    while opcion not in [1,2,3,4,5]:
      print(jug1,'ha cantado ENVIDO')
      print('\n',jug2,', que desea hacer?')
      print('1. Envido')
      print('2. Real envido')
      print('3. Falta envido')
      print('4. Quiero')
      print('5. No quiero')
      opcion = int(input('\tElija (recuerde, sus opciones son 1-2-3-4-5):'))


    if opcion == 1:              #ENVIDO (j1) ENVIDO (j2)
      puntos_al_no = puntos_tanto
      puntos_tanto = 4
      print(jug2,'ha cantado ENVIDO')
      print('\n',jug1,', que desea hacer?')
      print('1. Real envido')
      print('2. Falta envido')
      print('3. Quiero')
      print('4. No quiero')
      opcion = int(input('\tElija:'))
      while opcion not in [1,2,3,4]:
        print(jug2,'ha cantado ENVIDO')
        print('\n',jug1,', que desea hacer?')
        print('1. Real envido')
        print('2. Falta envido')
        print('3. Quiero')
        print('4. No quiero')
        opcion = int(input('\tElija (recuerde, sus opciones son 1-2-3-4):'))

      if opcion == 1:              #ENVIDO (j1) ENVIDO (j2) REAL ENVIDO (j1)
        puntos_al_no = puntos_tanto
        puntos_tanto = 7
        puntos1, puntos2 = real_envido (jug1, puntos1, jug2, puntos2, puntos_tanto, puntos_al_no)
        
      elif opcion == 2:                   #ENVIDO (j1) ENVIDO (j2) FALTA ENVIDO (j1)
        puntos_al_no=4
        puntos1, puntos2 = falta_envido (jug1, puntos1, jug2, puntos2, puntos_al_no)
      
      elif opcion == 3:                   # ENVIDO (j1) ENVIDO (j2) QUIERO (j1)
        print('\n',jug1,' ha dicho QUIERO')
        puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto)
      
      elif opcion == 4:                   # ENVIDO (j1) ENVIDO (j2) NO QUIERO (j1)
        print('\n',jug1,' ha dicho NO QUIERO.',jug2,'suma',puntos_tanto,'puntos')
        puntos2 += puntos_al_no
    
    elif opcion == 2:                     #ENVIDO (j1) REAL ENVIDO (j2)
      puntos_al_no = puntos_tanto
      puntos_tanto=5
      puntos1, puntos2 = real_envido (jug2, puntos2, jug1, puntos1, puntos_tanto, puntos_al_no)
      
    elif opcion == 3:                     #ENVIDO (j1) FALTA ENVIDO (j2)
      puntos_al_no=2
      puntos1, puntos2 = falta_envido (jug2, puntos2, jug1, puntos1, puntos_al_no)
    
    elif opcion == 4:                     #ENVIDO (j1) QUIERO (j2)
      print('\n',jug2,' ha dicho QUIERO')
      puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto)
    
    elif opcion == 5:                     #ENVIDO (j1) NO QUIERO (j2)
      print('\n',jug2,' ha dicho NO QUIERO.',jug1,'suma',puntos_tanto,'puntos')
      puntos1 += puntos_al_no
    
  elif opcion == 2:                     #REAL ENVIDO (j1) 
    puntos_al_no = 1
    puntos_tanto = 32
    puntos1, puntos2 = real_envido (jug1, puntos1, jug2, puntos2, puntos_tanto, puntos_al_no)
  
  elif opcion == 3:
    puntos_al_no=1
    puntos1, puntos2 = falta_envido (jug1, puntos1, jug2, puntos2, puntos_al_no)
  
  return puntos1, puntos2

