from random import shuffle, randint
from datetime import date
print(date.today()) 
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
    def __init__ (self, resultado : str,jugadores, lista_partidas):
        self.fecha = date.today()
        self.codigo_partida = Partida.asignar_codigo (lista_partidas)
        self.resultado = resultado
        self.jugadores = jugadores
    def asignar_codigo (self, lista_partidas):
        return max(lista_partidas) + 1

    def __str__ (self) -> str:
        return "La partida {} entre {} y {} salio {} y ocurrio el dia: {}".format(self.codigo_partida, self.jugadores[0], self.jugadores[1], self.resultado, self.fecha)
    

class Partidas():
    def __init__ (self) -> None:
      self.lista_partidas = []
    def agrega_partida (self, ):
       self.lista_partidas.append (Partida.codigo_partida)
