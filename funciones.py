from Clases import *
from MAIN import *
from envido import *

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

def mostrar_cartas(lista):
    cartas = ""
    for i in lista:
        cartas += (str(i))
    return "sus cartas son {}".format(cartas)

def tirar_3 (jugador,cartas):
    lista = []
    print(jugador + mostrar_cartas(cartas))
    print("Que carta desea tirar:")
    print("0."+cartas[0])
    print("1."+cartas[1])
    print("2."+cartas[2])
    op = int(input("Elija:"))
    while op not in [0,1,2]:
        print(jugador + mostrar_cartas(cartas))
        print("Que carta desea tirar:")
        print("0."+cartas[0])
        print("1."+cartas[1])
        print("2."+cartas[2])
        op = int(input("Elija entre 0,1,2:"))
    for j in cartas:
        if j != cartas[op]:
            lista.append(j)
    return cartas[op],lista

def tirar_2(jugador,cartas):
    lista = []
    print(jugador + mostrar_cartas(cartas))
    print("Que carta desea tirar:")
    print("0."+cartas[0])
    print("1."+cartas[1])
    op = int(input("Elija:"))
    while op not in [0,1]:
        print("Que carta desea tirar:")
        print("0."+cartas[0])
        print("1."+cartas[1])
        op = int(input("Elija entre 0,1:"))
    for j in cartas:
        if j != cartas[op]:
            lista.append(j)
    return cartas[op],lista

def tirar_1(jugador,cartas):
    lista = []
    print(jugador + mostrar_cartas(cartas))
    print("Le queda una sola carta, presione 0 para tirarla:")
    print("0."+cartas[0])
    op = int(input("Elija:"))
    while op != 0:
        op = int(input("Elija 0:"))
    return cartas[op]


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