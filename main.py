from time import sleep

while True:

    print("Bienvenido")

    print("-----------------------------------")
    sleep(1)

    print("Estas en una isla y debes explorarla elije sabiamente a donde dirigirte ....")

    op1 = int(input(" 1. Derecha\n 2. Izquierda\n"))

    if op1 == 1:
        print("Caes en un agujero lleno de pinchos y mueres ... F en el chat")

    elif op1 == 2:
        print("llegas a una laguna ahora debes escoger...")
        op2 = int(input(" 1. Nadar \n 2. Esperar \n 3. Correr \n"))

        print("-----------------------------------")

        if op2 == 1:
            print(
                "Llegas a la orilla y una tribu de canivales te vuelven guiso paisa .... F en el chat")
        elif op2 == 2:
            print("Te alcanza un rayo y mueres electrocutado ... F en el chat")

        elif op2 == 3:
            print("-----------------------------------")
            print("Luego de esperar un tiempo debes escoger...")

            op3 = int(input("1. Continuar caminando \n 2. Dormir \n 3. Comer \n"))

            if op3 == 2:
                print(
                    "Te secuestran unos micos y te hacen pure de banana ... F en el chat")
            elif op3 == 3:
                print(
                    "Comes unas lindas y redonditas moras pero estas estan envenenadas ... F en el chat")

            elif op3 == 1:
                print("-----------------------------------")
                print("Caen unas puertas enormes cielo ahora debes escoger ...")

                op4 = int(
                    input(" 1. Amarilla \n 2. Roja \n 3. Azul \n 4. Morado \n"))

                if op4 == 2:
                    print(
                        "Ardes en llamas y te reencuentras con la reina Isabel II ... F en el chat")

                elif op4 == 3:
                    print(
                        "Aparece una bestia enorme igualita a Maria Fernanda Cabal mueres del susto ... F en el chat")

                elif op4 == 4:
                    print(
                        "Aparece una serpiente venenosa y te envenena ... F en el chat")

                elif op4 == 1:
                    print(
                        "Hay un cofre lleno de oro ahora eres rico ¡Felicidades no tienes que trabajar en un call center!")
    else:
        print("gg vuelve a jugar :D")
