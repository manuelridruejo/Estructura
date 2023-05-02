import funciones as F
import MAIN as M 

def real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano):
  
  print('\n' + jug1, 'ha cantado REAL ENVIDO')
  F.mostrar_cartas (cartasj2)
  print('\n' + jug2 + ', que desea hacer?')
  print('1. Falta envido')
  print('2. Quiero')
  print('3. No quiero')
  opcion = (input('Elija: '))

  while opcion not in [1, 2, 3]:
    opcion = (input('Por favor, elija 1, 2 o 3: '))

  if opcion == 1:                   
    puntos_al_no=puntos_tanto
    puntos1, puntos2 = falta_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_al_no, mano)
    
  elif opcion == 2:                    
    print('\n' + jug2 + ' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
    
  elif opcion == 3:                
    print('\n' + jug2 + ' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
    puntos1 += puntos_al_no
    M.registro_partidas.write(jug1, 'suma', puntos_al_no, 'puntos de tanto')
  
  return puntos1, puntos2


def falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano):
  
  puntos_tanto = contar_puntos_falta (puntos1,puntos2)

  print('\n'+jug1,'ha cantado FALTA ENVIDO!')
  F.mostrar_cartas (cartasj2)
  print('\n' + jug2 + ', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = (input('Elija:'))
  
  while opcion not in [1, 2]:
    opcion = (input('Por favor, elija 1 o 2: '))

  if opcion == 1:                         
    print('\n' + jug2 + ' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
          
  if opcion == 2:                         
    print('\n' + jug2 + ' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
    puntos1 += puntos_al_no
    M.registro_partidas.write(jug1, 'suma', puntos_al_no, 'puntos de tanto')
  
  return puntos1, puntos2


def contar_tanto(cartas):
    
    tanto_01 = 0
    tanto_02 = 0
    tanto_12 = 0
    n=0

    if cartas[1].palo == cartas[2].palo:
      tanto_12 = 20 + (int(cartas[1].jerarquia_envido) + int(cartas[2].jerarquia_envido))
      n += 1

    if cartas[0].palo == cartas[1].palo:
      tanto_01 = 20 + (int(cartas[1].jerarquia_envido) + int(cartas[0].jerarquia_envido))
      n += 1
        
    if cartas[0].palo == cartas[2].palo:
      tanto_02 = 20 + (int(cartas[0].jerarquia_envido) + int(cartas[2].jerarquia_envido))
        
    if n >= 1:
      tanto = max (tanto_01, tanto_02, tanto_12)

    if n == 0:
      tanto = (max (cartas[0].jerarquia_envido, cartas[1].jerarquia_envido, cartas[2].jerarquia_envido))
    
    return tanto


def contar_los_tantos (cartasjug1, cartasjug2):
  
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


def sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano):
  
  tanto1, tanto2 = contar_los_tantos (cartasj1, cartasj2) 

  if jug1 == mano:
    print('\n' + jug1 + ':',tanto1)

    if tanto2>tanto1:
      print(jug2 + ':', tanto2, 'son mejores!!')
      puntos2 += puntos_tanto
      print(jug2, 'suma', puntos_tanto, 'puntos de tanto')
      M.registro_partidas.write(jug2, 'suma', puntos_tanto, 'puntos de tanto') 

    else:
      print(jug2 + ': son buenas.')
      puntos1 += puntos_tanto
      print(jug1, 'suma', puntos_tanto, 'puntos de tanto')
      M.registro_partidas.write(jug1, 'suma', puntos_tanto, 'puntos de tanto') 

  elif jug2 == mano:
    print('\n' + jug2 + ':',tanto2)

    if tanto1 > tanto2:
      print(jug1 + ':', tanto1, 'son mejores!!')
      puntos1 += puntos_tanto
      print(jug1, 'suma', puntos_tanto, 'puntos')
      M.registro_partidas.write(jug1, 'suma', puntos_tanto, 'puntos de tanto') 

    else:
      print(jug1 + ': son buenas.')
      puntos2 += puntos_tanto
      print(jug2, 'suma', puntos_tanto, 'puntos')
      M.registro_partidas.write(jug2, 'suma', puntos_tanto, 'puntos de tanto') 

  return puntos1, puntos2
  

def envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano):
  
  print('\nQue desea cantar?')
  print('1. Envido')
  print('2. Real envido')
  print('3. Falta envido')
  opcion = (input('Elija: '))

  while opcion not in [1, 2, 3]:
    opcion = (input('Por favor, elija 1, 2 o 3: '))

  if opcion == 1:          
    puntos_tanto = 2
    puntos_al_no = 1
    print('\n' + jug1,'ha cantado ENVIDO')
    print('\n' + jug2 + ', que desea hacer?')
    F.mostrar_cartas (cartasj2)
    print('1. Envido')
    print('2. Real envido')
    print('3. Falta envido')
    print('4. Quiero')
    print('5. No quiero')
    opcion = (input('Elija: '))

    while opcion not in [1, 2, 3, 4, 5]:
      opcion = (input('Por favor, elija 1, 2, 3, 4 o 5: '))

    if opcion == 1:             
      puntos_al_no = puntos_tanto
      puntos_tanto = 4
      print('\n' + jug2, 'ha cantado ENVIDO')
      F.mostrar_cartas (cartasj2)
      print('\n' + jug1 + ', que desea hacer?')
      print('1. Real envido')
      print('2. Falta envido')
      print('3. Quiero')
      print('4. No quiero')
      opcion = (input('Elija: '))

      while opcion not in [1, 2, 3, 4]:
        opcion = (input('Por favor, elija 1, 2, 3 o 4: '))

      if opcion == 1:            
        puntos_al_no = puntos_tanto
        puntos_tanto = 7
        puntos1, puntos2 = real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano)
        
      elif opcion == 2:                 
        puntos_al_no=4
        puntos1, puntos2 = falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
      
      elif opcion == 3:                 
        print('\n' + jug1 + ' ha dicho QUIERO')
        puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
      
      elif opcion == 4:                 
        print('\n' + jug1 + ' ha dicho NO QUIERO.',jug2,'suma',puntos_al_no,'puntos')
        puntos2 += puntos_al_no
        M.registro_partidas.write(jug2, 'suma', puntos_al_no, 'puntos de tanto')
    
    elif opcion == 2:                  
      puntos_al_no = puntos_tanto
      puntos_tanto=5
      puntos1, puntos2 = real_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_tanto, puntos_al_no, mano)
      
    elif opcion == 3:          
      puntos_al_no=2
      puntos1, puntos2 = falta_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_al_no, mano)
    
    elif opcion == 4:               
      print('\n' + jug2 + ' ha dicho QUIERO')
      puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
    
    elif opcion == 5:                  
      print('\n' + jug2 + ' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
      puntos1 += puntos_al_no
      M.registro_partidas.write(jug1, 'suma', puntos_al_no, 'puntos de tanto')
    
  elif opcion == 2:                    
    puntos_al_no = 1
    puntos_tanto = 32
    puntos1, puntos2 = real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano)
  
  elif opcion == 3:
    puntos_al_no=1
    puntos1, puntos2 = falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
  
  return puntos1, puntos2