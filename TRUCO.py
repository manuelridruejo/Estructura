def CantarTruco (p1, p2): 

  termino = False
  ganador = ''

  print('\n' + p1, 'ha cantado TRUCO!')
  print('\n' + p2 + ', que desea hacer?')
  print('1. Retruco')
  print('2. Quiero')
  print('3. No quiero')
  opcion = (input('Elija:'))

  while opcion not in ['1', '2', '3']:
    opcion = (input('Por favor, elija 1, 2 o 3: '))
  opcion = int(opcion)

  if opcion == 1:
    puntos_truco, termino, ganador, quiero = CantarReTruco (p2, p1)
  
  elif opcion == 2:
    print('\n' + p2 + ', ha dicho QUIERO')
    puntos_truco = 2
    quiero = p2
          
  elif opcion == 3:
    print('\n' + p2 + ', ha dicho NO QUIERO')
    puntos_truco = 1
    termino = True
    ganador = p1
    quiero = 'no'
  
  return puntos_truco, termino, ganador, quiero

def CantarReTruco (p1, p2):

  termino = False
  ganador = ''

  print('\n' + p1, 'ha cantado RE TRUCO!')
  print('\n' + p2 + ', que desea hacer?')
  print('1. Vale cuatro')
  print('2. Quiero')
  print('3. No quiero')
  opcion = (input('Elija:'))

  while opcion not in ['1', '2', '3']:
    opcion = (input('Por favor, elija 1, 2 o 3: '))
  opcion = int(opcion)

  if opcion == 1:
    puntos_truco, termino, ganador, quiero = CantarValeCuatro (p2, p1)
  
  elif opcion == 2: 
    print('\n' + p2 + ', ha dicho QUIERO')
    puntos_truco = 3
    quiero = p2

  elif opcion == 3:
    print('\n' + p2 + ', ha dicho NO QUIERO')
    puntos_truco = 2
    termino = True
    ganador = p1
    quiero = 'no'

  return puntos_truco, termino, ganador, quiero

def CantarValeCuatro (p1, p2):
  
  termino = False
  ganador = ''

  print('\n' + p1, 'ha cantado QUIERO VALE CUATRO!')
  print('\n' + p2 + ', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = (input('Elija:'))

  while opcion not in ['1', '2']:
    opcion = (input('Por favor, elija 1 o 2: '))
  opcion = int(opcion)

  if opcion == 1:
    print('\n' + p2 + ', ha dicho QUIERO')
    puntos_truco = 4
    quiero = p2
  
  elif opcion == 2:
    print('\n' + p2 + ', ha dicho NO QUIERO')
    puntos_truco = 3
    termino = True
    ganador = p1
    quiero = 'no'

  return puntos_truco, termino, ganador, quiero