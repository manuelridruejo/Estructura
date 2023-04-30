def CantarTruco (p1,p2): 
  retruco = False
  vale_cuatro = False
  quiero = True

  print(p1,'ha cantado TRUCO!')
  print(p2+', que desea hacer?')
  print('1. Retruco')
  print('2. Quiero')
  print('3. No quiero')
  opcion = int(input('\tElija:'))

  if opcion == 1:
    retruco = True 
    print(p2,'ha cantado RE TRUCO!')
    print(p1+', que desea hacer?')
    print('1. Vale cuatro')
    print('2. Quiero')
    print('3. No quiero')
    opcion = int(input('\tElija:'))

    if opcion == 1:
      vale_cuatro = True
      print(p1,'ha cantado QUIERO VALE CUATRO!')
      print(p2+', que desea hacer?')
      print('1. Quiero')
      print('2. No quiero')
      opcion = int(input('\tElija:'))

      if opcion == 1:
        print(p2+', ha dicho QUIERO')
        puntos_truco = 4
      
      elif opcion == 2:
        print(p2+', ha dicho NO QUIERO')
        puntos_truco = 3
        quiero = False
    
    elif opcion == 2:
      print(p1+', ha dicho QUIERO')
      puntos_truco = 3

    elif opcion == 3:
      print(p1+', ha dicho NO QUIERO')
      puntos_truco = 2
      quiero = False
  
  elif opcion == 2:
    print(p2+', ha dicho QUIERO')
    puntos_truco = 2
          
  elif opcion == 3:
    print(p2+', ha dicho NO QUIERO')
    puntos_truco = 1
    quiero = False
  
  return puntos_truco, quiero, retruco, vale_cuatro 

def CantarReTruco (p1, p2):
  print(p2,'ha cantado RE TRUCO!')
  print(p1+', que desea hacer?')
  print('1. Vale cuatro')
  print('2. Quiero')
  print('3. No quiero')
  opcion = int(input('\tElija:'))

  if opcion == 1:
    vale_cuatro = True
    print(p1,'ha cantado QUIERO VALE CUATRO!')
    print(p2+', que desea hacer?')
    print('1. Quiero')
    print('2. No quiero')
    opcion = int(input('\tElija:'))

    if opcion == 1:
      print(p2+', ha dicho QUIERO')
      puntos_truco = 4
    
    elif opcion == 2:
      print(p2+', ha dicho NO QUIERO')
      puntos_truco = 3
      quiero = False
  
  elif opcion == 2: 
    print(p1+', ha dicho QUIERO')
    puntos_truco = 3

  elif opcion == 3:
    print(p1+', ha dicho NO QUIERO')
    puntos_truco = 2
    quiero = False

  return puntos_truco, quiero, vale_cuatro

def CantarValeCuatro(p1, p2):
  print(p1,'ha cantado QUIERO VALE CUATRO!')
  print(p2+', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = int(input('\tElija:'))

  if opcion == 1:
    print(p2+', ha dicho QUIERO')
    puntos_truco = 4
  
  elif opcion == 2:
    print(p2+', ha dicho NO QUIERO')
    puntos_truco = 3
    quiero = False

  return puntos_truco, quiero