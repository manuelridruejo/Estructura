from random import shuffle, randint
from datetime import date
 
PALOS = ["Oro", "Espada", "Copa", "Basto"] # Variable global en mayúsculas Guía PEP-8
NUMEROS = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
JERARQUIAS = {
  ("Oro", 1): 7,
  ("Oro", 2): 8,
  ("Oro", 3): 9,
  ("Oro", 4): 0,
  ("Oro", 5): 1,
  ("Oro", 6): 2,
  ("Oro", 7): 10,
  ("Oro", 10): 4,
  ("Oro", 11): 5,
  ("Oro", 12): 6,
  ("Espada", 1): 13,
  ("Espada", 2): 8,
  ("Espada", 3): 9,
  ("Espada", 4): 0,
  ("Espada", 5): 1,
  ("Espada", 6): 2,
  ("Espada", 7): 11,
  ("Espada", 10): 4,
  ("Espada", 11): 5,
  ("Espada", 12): 6,
  ("Basto", 1): 12,
  ("Basto", 2): 8,
  ("Basto", 3): 9,
  ("Basto", 4): 0,
  ("Basto", 5): 1,
  ("Basto", 6): 2,
  ("Basto", 7): 3,
  ("Basto", 10): 4,
  ("Basto", 11): 5,
  ("Basto", 12): 6,
  ("Copa", 1): 7,
  ("Copa", 2): 8,
  ("Copa", 3): 9,
  ("Copa", 4): 0,
  ("Copa", 5): 1,
  ("Copa", 6): 2,
  ("Copa", 7): 3,
  ("Copa", 10): 4,
  ("Copa", 11): 5,
  ("Copa", 12): 6
}

JERARQUIAS_ENVIDO = {
  ("Oro", 1): 1,
  ("Oro", 2): 2,
  ("Oro", 3): 3,
  ("Oro", 4): 4,
  ("Oro", 5): 5,
  ("Oro", 6): 6,
  ("Oro", 7): 7,
  ("Oro", 10): 0,
  ("Oro", 11): 0,
  ("Oro", 12): 0,
  ("Espada", 1): 1,
  ("Espada", 2): 2,
  ("Espada", 3): 3,
  ("Espada", 4): 4,
  ("Espada", 5): 5,
  ("Espada", 6): 6,
  ("Espada", 7): 7,
  ("Espada", 10): 0,
  ("Espada", 11): 0,
  ("Espada", 12): 0,
  ("Basto", 1): 1,
  ("Basto", 2): 2,
  ("Basto", 3): 3,
  ("Basto", 4): 4,
  ("Basto", 5): 5,
  ("Basto", 6): 6,
  ("Basto", 7): 7,
  ("Basto", 10): 0,
  ("Basto", 11): 0,
  ("Basto", 12): 0,
  ("Copa", 1): 1,
  ("Copa", 2): 2,
  ("Copa", 3): 3,
  ("Copa", 4): 4,
  ("Copa", 5): 5,
  ("Copa", 6): 6,
  ("Copa", 7): 7,
  ("Copa", 10): 0,
  ("Copa", 11): 0,
  ("Copa", 12): 0
}


class Carta():
  def __init__ (self, palo : str, numero : int):
    self.palo = palo
    self.numero = numero
    self.jerarquia = JERARQUIAS[(palo, numero)]
    self.jerarquia_envido = JERARQUIAS_ENVIDO [(palo, numero)]

  def __str__ (self):
    return "{} de {}".format(self.numero, self.palo)
  
  def __eq__ (self, other):
    return self.jerarquia == other.jerarquia 
  
  def __gt__ (self, other):
    return self.jerarquia > other.jerarquia

  def __lt__ (self, other):
    return self.jerarquia < other.jerarquia 
  
  def __ge__ (self, other):
    return self.jerarquia >= other.jerarquia 
  
  def __le__ (self, other):
    return self.jerarquia <= other.jerarquia 
  
  def __ne__ (self, other):
    return self.jerarquia != other.jerarquia 

  def __repr__ (self):
    return str (self)
    

class Mazo():
  def __init__(self) -> None:
    self.cartas = []
    for palo in PALOS:
      for numero in NUMEROS:
        self.cartas.append (Carta(palo, numero))
    self.mezclar()
  
  def __str__(self):
    impresion_mazo = ""
    for carta in self.cartas:
      impresion_mazo += (str(carta) + "\n")
    impresion_mazo = impresion_mazo[:-1]
    return impresion_mazo
  
  def mezclar (self):
    shuffle (self.cartas)
  
  def repartir (self):
    cartas=[]
    for i in range(6):
      cartas.append (self.cartas[i])
    return cartas

  
class Jugador():
    def __init__ (self, nombre : str, apellido : str, DNI):
          self.nombre = nombre
          self.apellido = apellido
          self.DNI= DNI


class Jugadores():

    def __init__ (self, lista_jugadores) -> None:
      self.lista_jugadores = lista_jugadores

    def agregar_jugadores (self,jugador):
      self.lista_jugadores.append (jugador.nombre_usuario)


class Partida():

    def __init__ (self, resultado : str, jugadores, lista_partidas):
        self.fecha = date.today()
        self.codigo_partida = self.asignar_codigo (lista_partidas)
        self.resultado = resultado
        self.jugadores = jugadores

    def asignar_codigo (self, lista_partidas):
        return max(lista_partidas) + 1

    def __str__ (self):
        return "La partida {} entre {} y {} , {} y ocurrio el dia: {}".format(self.codigo_partida, self.jugadores[0], self.jugadores[1], self.resultado, self.fecha)
    

class Partidas():
    def __init__ (self) -> None:
      self.lista_partidas = []
    def agrega_partida (self, ):
       self.lista_partidas.append (Partida.codigo_partida)





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






def real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano):
  
  print('\n' + jug1, 'ha cantado REAL ENVIDO')
  mostrar_cartas (cartasj2)
  print('\n' + jug2 + ', que desea hacer?')
  print('1. Falta envido')
  print('2. Quiero')
  print('3. No quiero')
  opcion = (input('Elija: '))

  while opcion not in ['1', '2', '3']:
    opcion = (input('Por favor, elija 1, 2 o 3: '))
  opcion = int(opcion)

  if opcion == 1:                   
    puntos_al_no=puntos_tanto
    puntos1, puntos2 = falta_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_al_no, mano)
    
  elif opcion == 2:                    
    print('\n' + jug2 + ' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
    
  elif opcion == 3:                
    print('\n' + jug2 + ' ha dicho NO QUIERO.', jug1, 'suma', puntos_al_no, 'puntos')
    puntos1 += puntos_al_no
    registro_partidas.write(jug1 + 'suma' + str(puntos_al_no) + 'puntos de tanto')
  
  return puntos1, puntos2


def falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano):
  
  puntos_tanto = contar_puntos_falta (puntos1,puntos2)

  print('\n'+jug1,'ha cantado FALTA ENVIDO!')
  mostrar_cartas (cartasj2)
  print('\n' + jug2 + ', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = (input('Elija:'))
  
  while opcion not in ['1', '2']:
    opcion = (input('Por favor, elija 1 o 2: '))
  opcion = int(opcion)

  if opcion == 1:                         
    print('\n' + jug2 + ' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
          
  if opcion == 2:                         
    print('\n' + jug2 + ' ha dicho NO QUIERO.', jug1, 'suma', puntos_al_no, 'puntos')
    puntos1 += puntos_al_no
    registro_partidas.write(jug1 + 'suma' + str(puntos_al_no) + 'puntos de tanto')
  
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
      registro_partidas.write(jug2 + 'suma' + str(puntos_tanto) + 'puntos de tanto') 

    else:
      print(jug2 + ': son buenas.')
      puntos1 += puntos_tanto
      print(jug1, 'suma', puntos_tanto, 'puntos de tanto')
      registro_partidas.write(jug1 + 'suma' + str(puntos_tanto) + 'puntos de tanto') 

  elif jug2 == mano:
    print('\n' + jug2 + ':',tanto2)

    if tanto1 > tanto2:
      print(jug1 + ':', tanto1, 'son mejores!!')
      puntos1 += puntos_tanto
      print(jug1, 'suma', puntos_tanto, 'puntos')
      registro_partidas.write(jug1 +'suma' + str(puntos_tanto) + 'puntos de tanto') 

    else:
      print(jug1 + ': son buenas.')
      puntos2 += puntos_tanto
      print(jug2, 'suma', puntos_tanto, 'puntos')
      registro_partidas.write(jug2 + 'suma' + str(puntos_tanto) + 'puntos de tanto') 

  return puntos1, puntos2
  

def envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano):
  
  print('\nQue desea cantar?')
  print('1. Envido')
  print('2. Real envido')
  print('3. Falta envido')
  opcion = (input('Elija: '))

  while opcion not in ['1', '2', '3']:
    opcion = (input('Por favor, elija 1, 2 o 3: '))
  opcion = int(opcion)

  if opcion == 1:          
    puntos_tanto = 2
    puntos_al_no = 1
    print('\n' + jug1,'ha cantado ENVIDO')
    print('\n' + jug2 + ', que desea hacer?')
    mostrar_cartas (cartasj2)
    print('1. Envido')
    print('2. Real envido')
    print('3. Falta envido')
    print('4. Quiero')
    print('5. No quiero')
    opcion = (input('Elija: '))

    while opcion not in ['1', '2', '3', '4', '5']:
      opcion = (input('Por favor, elija 1, 2, 3, 4 o 5: '))
    opcion = int(opcion)

    if opcion == 1:             
      puntos_al_no = puntos_tanto
      puntos_tanto = 4
      print('\n' + jug2, 'ha cantado ENVIDO')
      mostrar_cartas (cartasj2)
      print('\n' + jug1 + ', que desea hacer?')
      print('1. Real envido')
      print('2. Falta envido')
      print('3. Quiero')
      print('4. No quiero')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3', '4']:
        opcion = (input('Por favor, elija 1, 2, 3 o 4: '))
      opcion = int(opcion)

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
        print('\n' + jug1 + ' ha dicho NO QUIERO.', jug2, 'suma', puntos_al_no, 'puntos')
        puntos2 += puntos_al_no
        registro_partidas.write(jug2 + 'suma' + str(puntos_al_no) + 'puntos de tanto')
    
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
      registro_partidas.write(jug1 + 'suma' + str(puntos_al_no) + 'puntos de tanto')
    
  elif opcion == 2:                    
    puntos_al_no = 1
    puntos_tanto = 32
    puntos1, puntos2 = real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano)
  
  elif opcion == 3:
    puntos_al_no=1
    puntos1, puntos2 = falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
  
  return puntos1, puntos2









def mostrar_cartas (lista):
  cartas = "sus cartas son: "
  for i in lista:
    cartas += (str(i) + ', ')
  print(cartas)


def tirar_3 (jugador, cartas):
  lista = []
  print("\n" + jugador + ", que carta desea tirar: ")
  print("1. " + str(cartas[0]))
  print("2. " + str(cartas[1]))
  print("3. " + str(cartas[2]))
  op = (input("Elija: "))

  while op not in ['1', '2', '3']:
    op = (input('Por favor, elija 1, 2 o 3: '))
  op = int(op)

  for j in cartas:
    if j != cartas[op-1]:
      lista.append(j)

  return cartas[op-1], lista


def tirar_2(jugador,cartas):
  
  lista = []
  
  print("\n" + jugador + ", que carta desea tirar: ")
  print("1. " + str(cartas[0]))
  print("2. " + str(cartas[1]))
  op = (input("Elija: "))
  
  while op not in ['1', '2']:
    op = (input('Por favor, elija 1 o 2: '))
  op = int(op)
  
  for j in cartas:
    if j != cartas [op-1]:
      lista.append(j)
  
  return cartas[op],lista

def tirar_1 (jugador, cartas):
  
  print('\n' + jugador + ", le queda una sola carta, presione 1 para tirarla: ")
  print("1." + str(cartas[0]))
  op = (input("Elija: "))
  
  while op != '1':
    op = (input("Elija 1: "))

  return cartas[0], []


def quien_es_mano (ronda, p1, puntos1, p2, puntos2):
  
  if ronda%2 == 0:
    mano = p1
    pie = p2
    puntos_mano = puntos1
    puntos_pie = puntos2

  if ronda%2 != 0:
    mano = p2
    pie = p1
    puntos_mano = puntos2
    puntos_pie = puntos1

  return mano, puntos_mano, pie, puntos_pie


def JugarPrimera (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_truco, quiero, mano):                 #JUGAR PRIMERA
  
  termino = False
  hubo_envido = False
  carta1_p1=''
  ganador = ''

  if quiero == jug1 or quiero == '':

    if puntos_truco == 1:
      print('\n'+jug1+', que desea hacer?')
      mostrar_cartas(cartasj1)
      print('1. Cantar envido')
      print('2. Cantar truco')
      print('3. Tirar carta')
      print('4. Irse al mazo') 
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3', '4']:
        opcion = (input('Por favor, elija 1, 2, 3 o 4: '))
      opcion = int(opcion)

      if opcion == 1:
        puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n'+jug1+', que desea hacer?')
        mostrar_cartas(cartasj1)
        print('1. Cantar truco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = (input('Elija: '))

        while opcion not in ['1', '2', '3']:
          opcion = (input('Por favor, elija 1, 2 o 3: '))
        opcion = int(opcion)  

        if opcion == 1:
          puntos_truco, termino, ganador, quiero = CantarTruco (jug1, jug2)
          
          if termino != True:
            carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
            print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
        
        elif opcion == 2:
          carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
          print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
      
        elif opcion == 3:
          termino = True
          ganador = jug2

      elif opcion == 2:
        puntos_truco, termino, ganador, quiero = CantarTruco (jug1, jug2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 4:
        termino = True
        ganador = jug2

    elif puntos_truco == 2:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar envido')
      print('2. Cantar retruco')
      print('3. Tirar carta')
      print('4. Irse al mazo') 
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3', '4']:
        opcion = (input('Por favor, elija 1, 2, 3 o 4: '))
      opcion = int(opcion)

      if opcion == 1:
        puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar retruco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = (input('Elija: '))

        while opcion not in ['1', '2', '3']:
          opcion = (input('Por favor, elija 1, 2 o 3: '))
        opcion = int(opcion)

        if opcion == 1:
          puntos_truco, termino, ganador, quiero = CantarReTruco (jug1, jug2)
      
          if termino != True:
            carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
            print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
      
        elif opcion == 2:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
      
        elif opcion == 3:
          termino = True
          ganador = jug2

      elif opcion == 2:
        puntos_truco, termino, ganador, quiero = CantarReTruco (jug1, jug2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 4:
        termino = True
        ganador = jug2
      
    elif puntos_truco == 3:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar envido')
      print('2. Cantar vale cuatro')
      print('3. Tirar carta')
      print('4. Irse al mazo') 
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3', '4']:
        opcion = (input('Por favor, elija 1, 2, 3 o 4: '))
      opcion = int(opcion)

      if opcion == 1:
        puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar vale cuatro')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = (input('Elija:'))

        while opcion not in ['1', '2', '3']:
          opcion = (input('Por favor, elija 1, 2 o 3: '))
        opcion = int(opcion)

        if opcion == 1:
          puntos_truco, termino, ganador, quiero = CantarValeCuatro (jug1, jug2)
      
          if termino != True:
            carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
            print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
      
        elif opcion == 2:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
        
        elif opcion == 3:
          termino = True
          ganador = jug2

      elif opcion == 2:
        puntos_truco, termino, ganador, quiero = CantarValeCuatro (jug1, jug2)
    
        if termino != True:
          carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 4:
        termino = True
        ganador = jug2
      
    elif puntos_truco == 4:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar envido')
      print('2. Tirar carta')
      print('3. Irse al mazo') 
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)

      if opcion == 1:
        puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Tirar carta')
        print('2. Irse al mazo')
        opcion = (input('Elija: '))

        while opcion not in ['1', '2']:
          opcion = (input('Por favor, elija 1 o 2: '))
        opcion = int(opcion)

        if opcion == 1:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
        
        elif opcion == 2:
          termino = True
          ganador = jug2

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2
  
  elif quiero == jug2:
    print('\n' + jug1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Cantar envido')
    print('2. Tirar carta')
    print('3. Irse al mazo') 
    opcion = (input('Elija: '))

    while opcion not in ['1', '2', '3']:
      opcion = (input('Por favor, elija 1, 2 o 3: '))
    opcion = int(opcion)

    if opcion == 1:
      puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
      hubo_envido = True
        
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2']:
        opcion = (input('Por favor, elija 1 o 2: '))
      opcion = int(opcion)

      if opcion == 1:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        termino = True
        ganador = jug2
    
    elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = jug2

  return puntos1, puntos2, puntos_truco, termino, hubo_envido, carta1_p1, cartasj1, ganador, quiero


def JugarPrimeraSinTanto (jug1, cartasj1, jug2, puntos_truco, quiero):                            #JUGAR PRIMERA SIN TANTO
  
  carta1_p1 = ''
  ganador = ''
  termino = False 

  if quiero == jug1 or quiero == '':

    if puntos_truco == 1:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)

      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarTruco (jug1, jug2)

        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2

    elif puntos_truco == 2:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = (input('Elija: '))
      
      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)

      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarReTruco (jug1, jug2)

        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2

    elif puntos_truco == 3:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)
      
      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarValeCuatro (jug1, jug2)
          
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2
    
    elif puntos_truco == 4:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2']:
        opcion = (input('Por favor, elija 1 0 2: '))
      opcion = int(opcion)

      if opcion == 1:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        termino = True
        ganador = jug2
  
  elif quiero == jug2:
    print('\n' + jug1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = (input('Elija: '))

    while opcion not in ['1', '2']:
      opcion = (input('Por favor, elija 1 o 2: '))
    opcion = int(opcion)

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
      print("\n{} ha tirado el {}".format (jug1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = jug2

  return puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero


def Jugar_Segunda(p1, puntos1, p2, puntos2, cartasj1, puntos_truco, quiero):                            #JUGAR SEGUNDA MANO
  
  termino= False
  carta1_p1 = ""
  ganador = ''

  if quiero == p1 or quiero == '':

    if puntos_truco == 1:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas(cartasj1)
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)
          
      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = CantarTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))
 
      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2 

    elif puntos_truco == 2:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)

      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = CantarReTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
          print("\n{} ha tirado el {}".format(p1,carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
        print("\n{} ha tirado el {}".format(p1, carta1_p1))
 
      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 3:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)

      if opcion == 1:     
        puntos_truco, termino, ganador, quiero = CantarValeCuatro (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 4:
      carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
      print("\n{} ha tirado el {}".format (p1, carta1_p1))
  
  elif quiero == p2:
    print('\n' + p1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = (input('Elija: '))

    while opcion not in ['1', '2']:
      opcion = (input('Por favor, elija 1 o 2: '))
    opcion = int(opcion)

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
      print("\n{} ha tirado el {}".format (p1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = p2
     
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero 


def Jugar_Tercera (p1, puntos1, p2, puntos2, cartasj1, puntos_truco, quiero):                #JUGAR TERCER MANO
  
  termino = False
  carta1_p1 = ""
  ganador = ''

  if quiero == p1 or quiero == '':

    if puntos_truco == 1:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)
      
      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 2:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)

      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = CantarReTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 3:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = (input('Elija: '))

      while opcion not in ['1', '2', '3']:
        opcion = (input('Por favor, elija 1, 2 o 3: '))
      opcion = int(opcion)

      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = CantarValeCuatro (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 4:
      carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
      print("\n{} ha tirado el {}".format (p1, carta1_p1))
   
  elif quiero == p2:
    print('\n' + p1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = (input('Elija: '))

    while opcion not in ['1', '2']:
      opcion = (input('Por favor, elija 1 o 2: '))
    opcion = int(opcion)

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_1(p1, cartasj1)
      print("\n{} ha tirado el {}".format(p1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = p2
     
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero 






registro_partidas = open("Registro partidas.txt", "r+") 
registro_jugadores = open("Registro Jugadores.txt", "r+")
registro_codigos = open("Registro codigos de partida.txt", "r+")
jugadores_archivo = registro_jugadores.read() 
codigos_archivo = registro_codigos.read()
#;1;jug1;jug2;20-04-2020;resultado;/;2;jug3;jug4;20-05-2020;resultado2;/2

#[[1,jug,jug2,20-04-2020,resultado],[2,jug3,jug4,20-05-2020,resultado2]]

cod = ""
lista_cod = []
for caracter in codigos_archivo:
  if caracter != "/":
    cod += caracter
  else:
    lista_cod.append(cod)
    cod = ""

cod2 = ""
lista_partidas_final = []

for codigo in lista_cod:
  aux = []
  for caracter in codigo:
    if caracter != ";":
      cod2 += caracter
    else:
      aux.append(cod2)
      cod2 = ""
  lista_partidas_final += [aux]

lista_codigos_existentes = []

for partida in lista_partidas_final:
  lista_codigos_existentes.append(int(partida[0]))


cadena_dni = ""
for i in jugadores_archivo:
  if i != "-":
    cadena_dni += i 

lista_dni =[]
for j in range(0, len(cadena_dni), 8):
  lista_dni.append(cadena_dni[j:j+8])


def Jugar():
  
  nombre1 = input("Ingrese el nombre de un jugador: ")
  apellido1= input("Y su apellido: ")

  dni1 = 0
  dni_mal = True
  while dni_mal == True:
    try:
      dni1 = int(input("Ingrese el DNI: ")) 
      while dni1 < 10000000 or dni1 > 99999999:
        dni1 = int(input("DNI invalido. Por favor, ingrese el DNI (8 numeros): ")) 
      dni_mal = False
    except:
      dni_mal = True

  nombre2 = input("\nIngrese el nombre del otro jugador: ")
  apellido2 = input("Y el apellido: ")

  dni2 = 0
  dni_mal = True
  while dni_mal == True:
    try:
      dni2 = int(input("Ingrese el DNI: ")) 
      while dni2 < 10000000 or dni2 > 99999999:
        dni2 = int(input("DNI invalido. Por favor, ingrese el DNI (8 numeros): ")) 
      dni_mal = False
    except:
      dni_mal = True

  jugador1 = Jugador (nombre1, apellido1, dni1)
  jugador2 = Jugador (nombre2, apellido2, dni2) 


  p1 = jugador1.nombre
  puntos1 = 0
  p2 = jugador2.nombre 
  puntos2 = 0
  ronda = 1

  if p1 == p2:
    p1 = jugador1.apellido
    p2 = jugador2.apellido

  escribir = "\nSe ha iniciado una nueva partida entre: " + p1 + " y " + p2

  print(escribir)
  registro_partidas.write(escribir)

  while puntos1 < 30 and puntos2 < 30:
    
    mazo=Mazo()       #Se crea el mazo

    cartas_en_juego = mazo.repartir()      #Se reparte el mazo

    mano, puntos_mano, pie, puntos_pie = quien_es_mano (ronda, p1, puntos1, p2, puntos2)        #Se determina que jugador es mano

    cartasmano = [cartas_en_juego[0],cartas_en_juego[2],cartas_en_juego[4]]         #Se dan las cartas al mano y al pie
    cartas_pie = [cartas_en_juego[1],cartas_en_juego[3],cartas_en_juego[5]]

    print('\nComienza la ronda '+str(ronda)+'!')

    print('\n'+mano, 'es MANO.')
    mostrar_cartas(cartasmano)
    print('\n')
    print(pie, 'es PIE.')
    mostrar_cartas(cartas_pie)
    puntos_truco = 1
    que_mano_es = 1
    hubo_envido = False
    termino = False
    quiero = ''

    while que_mano_es < 4:
      
      manos_pie = 0
      manos_mano = 0
      ganador1 = ''
      ganador2 = ''
      parda1 = False
      parda2 = False                 

      #Primera mano

      puntos_mano, puntos_pie, puntos_truco, termino, hubo_envido, carta1_mano, cartas_mano, ganador, quiero  = JugarPrimera (mano, puntos_mano, cartasmano, pie, puntos_pie, cartas_pie, puntos_truco, quiero, mano)
      
      if termino == True:
        if quiero == '':
          puntos_truco = 2
        break
      
      if hubo_envido == True:
        puntos_truco, termino, carta1_pie, cartas_pie, ganador, quiero  = JugarPrimeraSinTanto (pie, cartas_pie, mano, puntos_truco, quiero)
    
        if termino == True: 
          break

      elif hubo_envido == False:
        puntos_pie, puntos_mano, puntos_truco, termino, hubo_envido, carta1_pie, cartas_pie, ganador, quiero  = JugarPrimera (pie, puntos_pie, cartas_pie, mano, puntos_mano, cartasmano, puntos_truco, quiero, mano)

        if termino == True:
          break

      if carta1_pie > carta1_mano:
        ganador1 = pie
        print('\n'+pie, "ha ganado la mano")
        manos_pie += 1 

      elif carta1_mano > carta1_pie:
        ganador1 = mano 
        print('\n'+mano, "ha ganado la mano")
        manos_mano += 1

      elif carta1_mano == carta1_pie:
        parda1=True
        print('\nSe ha pardado')

      #Segunda Mano

      que_mano_es += 1

      if ganador1 == pie: #el pie gano primera arranca 2 el
        
        puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)

        if termino == True: 
          break

        puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

      elif ganador1 == mano: #la mano gano primera arranca la 2 el
        
        puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

        puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break

      elif  parda1 == True: #Se juega la parda
        
        puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        if carta2_mano == carta2_pie: #Se pardo segunda
          parda2 = True
          print("\nSe ha pardado")

        elif carta2_mano > carta2_pie: #gano la mano
          ganador = mano
          break
        
        elif carta2_pie > carta2_mano: #gano el pie
          ganador = pie
          break 
        
      if carta2_mano > carta2_pie: #mano gana segunda
        ganador2 = mano
        print('\n'+mano, "ha ganado la mano")
        manos_mano += 1

      elif carta2_pie > carta2_mano: #pie gana segunda
        ganador2 = pie
        manos_pie += 1
        print('\n'+pie, "ha ganado la mano")

      elif carta2_pie == carta2_mano and parda1 == False: #se parda 2 y no esta pardada primera
        if ganador1 == pie:
          ganador = pie
          break

        elif ganador1 == mano:
          ganador = mano

      if manos_pie == 2:
        ganador = pie
        break

      if manos_mano == 2:
        ganador = mano
        break 

      # Tercera Mano 
      
      que_mano_es += 1

      if ganador2 == pie:                 #pie gana 2 arranca en 3
      
        puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)

        if termino == True: 
          break

        puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

      elif ganador2 == mano: #mano gano 2 arranca en 3
        puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

        puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break
        
      elif  parda2 == True and parda1 == True: #Se juega la parda
        puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        if carta3_mano == carta3_pie: #Se pardo tercera gana la mano
          ganador = mano

        elif carta3_mano > carta3_pie: #gano la mano
          ganador = mano
        
        elif carta3_pie > carta3_mano: #gano el pie
          ganador = pie
        
      elif carta3_mano > carta3_pie: #gano la mano la 3 se le suman los puntos
        ganador = mano
        break

      elif carta3_pie > carta3_mano: #gano el pie la tercera se le suman los puntos
        ganador = pie
        break

      que_mano_es += 1

    if ganador == mano:
      puntos_mano += puntos_truco
      print("\nHa ganado: ", mano, " se le suman ", puntos_truco, " puntos")
      registro_partidas.write("\nHa ganado: " + mano + " se le suman " + str(puntos_truco) + " puntos") 
      
    elif ganador == pie:
      puntos_pie += puntos_truco
      print("\nHa ganado: ", pie, " se le suman ", puntos_truco, " puntos")
      registro_partidas.write("\nHa ganado: " + pie + " se le suman " + str(puntos_truco) + " puntos") 

    if p1 == mano:
      puntos1 = puntos_mano
      puntos2 = puntos_pie
    elif p2 == mano:
      puntos2 = puntos_mano
      puntos1 = puntos_pie
    
    print('\nPuntos de '+ p1 + ": " + str(puntos1))
    print('\nPuntos de ' + p2 + ": " + str(puntos2))
    print('\n------------------------------------------------------------------------------\n\n')
    registro_partidas.write('\nPuntos de ' + p1 + ": " + str(puntos1))
    registro_partidas.write('\nPuntos de ' + p2 + ": " + str(puntos2))
    registro_partidas.write('\n------------------------------------------------------------------------------\n\n')

    ronda +=1


  if puntos1 >= 30 and puntos2 >= 30:
          
    if puntos1 > puntos2:
      print('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
      registro_partidas.write('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
      ganador_final = "gano {}, {} a {}".format(p1, puntos1, puntos2) 
    elif puntos2 > puntos1:
      print('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
      registro_partidas.write('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
      ganador_final = "gano {}, {} a {}".format(p2, puntos2, puntos1) 
    elif puntos2 == puntos1:
      print('\nHA HABIDO UN EMPATE.')
      registro_partidas.write('\nHA HABIDO UN EMPATE.')
      ganador_final = "empate"
  elif puntos2 >= 30:
    print('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
    registro_partidas.write('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
    ganador_final = "gano {}, {} a {}".format(p2, puntos2, puntos1) 

  elif puntos1 >= 30:
    print('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
    registro_partidas.write('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
    ganador_final = "gano {}, {} a {}".format(p1, puntos1, puntos2)


  dni_a_agregar=[jugador1.DNI, jugador2.DNI]
  for f in dni_a_agregar:
    if f not in lista_dni:
      registro_jugadores.write("-" + str(f) + "-")


  partida_jugada = Partida(ganador_final, [jugador1.nombre,jugador2.nombre], lista_codigos_existentes)
  escritura = "{};{};{};{};{};/".format(str(partida_jugada.codigo_partida), partida_jugada.jugadores[0], partida_jugada.jugadores[1], partida_jugada.fecha, partida_jugada.resultado)
  registro_codigos.write(escritura)

opcion2 = 1
while opcion2 != 3:

  print("\nBienvenido! ¿Qué desea hacer?")
  print("\n1. Buscar una partida")
  print("\n2. Jugar un partido de Truco")
  print("\n3. Salir")
  opcion2 = input("\nElija: ")

  while opcion2 not in ['1', '2', '3']:
    opcion2 = input("Error. Elija entre 1,2 o 3: ")
  opcion2 = int(opcion2)
  
  
  if opcion2 == 1:
    codigo_correcto = False
    while codigo_correcto == False:
      try:
        codigo_a_buscar = int(input("Por favor ingrese el codigo de partida: "))
        while codigo_a_buscar not in lista_codigos_existentes:
          codigo_a_buscar = int(input("Error. Intente nuevamente. Por favor ingrese el codigo de partida: "))
        codigo_correcto = True
      
      except:
        codigo_correcto = False
    
    for partida in lista_partidas_final:
      #print(partida)
      if codigo_a_buscar == int(partida[0]):
        partida_encontrada = partida

    impresion = "La partida {} entre {} y {} salio {} y ocurrio el dia: {}".format(partida_encontrada[0],partida_encontrada[1], partida_encontrada[2], partida_encontrada[4], partida_encontrada[3])
    print(impresion)
  
  elif opcion2 == 2:
    Jugar()



registro_partidas.close() 
registro_jugadores.close()
registro_codigos.close()
