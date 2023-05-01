
def JugarPrimera (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_truco):
    termino = False
    hubo_envido = False
    carta1_p1=''

    if puntos_truco == 1:
        print(jug1+', que desea hacer?')
        print('1. Cantar envido')
        print('2. Cantar truco')
        print('3. Tirar carta')
        print('4. Irse al mazo') 
        opcion = int(input('Elija:'))

        if opcion == 1:
            puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
            hubo_envido = True
            
            print('\n'+jug1+', que desea hacer?')
            print('1. Cantar truco')
            print('2. Tirar carta')
            print('3. Irse al mazo')
            opcion = int(input('Elija:'))

        if opcion == 1:
            puntos_truco, quiero = CantarTruco (jug1, jug2)
        
            if quiero == False:
                termino = True
            
            else:
                carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
                print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
        
        elif opcion == 2:
            carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
            print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
        
        elif opcion == 3:
            termino = True

        elif opcion == 2:
            puntos_truco, quiero = CantarTruco (jug1, jug2)
        
        if quiero == False:
            termino = True
        
        else:
            carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
            print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
        print("\{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 4:
        termino = True

    elif puntos_truco == 2:
        print(jug1+', que desea hacer?')
        print('1. Cantar envido')
        print('2. Cantar retruco')
        print('3. Tirar carta')
        print('4. Irse al mazo') 
        opcion = int(input('Elija:'))

        if opcion == 1:
            puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
            hubo_envido = True
            
            print('\n'+jug1+', que desea hacer?')
            print('1. Cantar retruco')
            print('2. Tirar carta')
            print('3. Irse al mazo')
            opcion = int(input('Elija:'))

        if opcion == 1:
            puntos_truco, quiero = CantarReTruco (jug1, jug2)
        
            if quiero == False:
                termino = True
            
            else:
                carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
                print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
        
        elif opcion == 2:
            carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
            print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
        
        elif opcion == 3:
            termino = True

        elif opcion == 2:
            puntos_truco, quiero = CantarReTruco (jug1, jug2)
        
        if quiero == False:
            termino = True
        
        else:
            carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
            print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
        print("\{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 4:
        termino = True
        
    elif puntos_truco == 3:
        print(jug1+', que desea hacer?')
        print('1. Cantar envido')
        print('2. Cantar vale cuatro')
        print('3. Tirar carta')
        print('4. Irse al mazo') 
        opcion = int(input('Elija:'))

        if opcion == 1:
            puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
            hubo_envido = True
            
            print('\n'+jug1+', que desea hacer?')
            print('1. Cantar vale cuatro')
            print('2. Tirar carta')
            print('3. Irse al mazo')
            opcion = int(input('Elija:'))

        if opcion == 1:
            puntos_truco, quiero = CantarValeCuatro (jug1, jug2)
        
            if quiero == False:
                termino = True
            
            else:
                carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
                print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
        
        elif opcion == 2:
            carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
            print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
        
        elif opcion == 3:
            termino = True

        elif opcion == 2:
            puntos_truco, quiero = CantarValeCuatro (jug1, jug2)
        
            if quiero == False:
                termino = True
            
            else:
                carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
                print("\n{} ha tirado el {}".format(jug1, carta1_p1))

        elif opcion == 3:
            carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
            print("\{} ha tirado el {}".format(jug1, carta1_p1))

        elif opcion == 4:
            termino = True
        
    elif puntos_truco == 4:
        print(jug1+', que desea hacer?')
        print('1. Cantar envido')
        print('2. Tirar carta')
        print('3. Irse al mazo') 
        opcion = int(input('Elija:'))

        if opcion == 1:
            puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
            hubo_envido = True
            
            print('\n'+jug1+', que desea hacer?')
            print('1. Tirar carta')
            print('2. Irse al mazo')
            opcion = int(input('Elija:'))
        
            if opcion == 1:
                carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
                print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
            
            elif opcion == 2:
                termino = True

            elif opcion == 2:
                carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
                print("\{} ha tirado el {}".format(jug1, carta1_p1))

            elif opcion == 3:
                termino = True

    return puntos1, puntos2, puntos_truco, termino, hubo_envido, carta1_p1, cartasj1