import random
def posicion_inicial_robot_x():
    while True:
        init_posicion_x=random.randint(0, 9)
        init_meta_x=random.randint(0, 9)
        if init_posicion_x!=init_meta_x:
            return init_posicion_x
        else:
            continue
def posicion_inicial_robot_y():
    while True:
        init_posicion_y=random.randint(0, 9)
        init_meta_y=random.randint(0, 9)
        if init_posicion_y!=init_meta_y  :
            return init_posicion_y
            break
        else:
            continue

def pos_derecha(posicion):
    limite=9
    posicion_nueva=posicion+1
    if posicion_nueva<=limite:
        posicion=posicion_nueva
        return posicion
    else:
        print("Estas fuera del limite")
        return posicion
def pos_abajo(posicion):
    limite=9
    posicion_nueva=posicion+1
    if posicion_nueva<=limite:
        posicion=posicion_nueva
        return posicion
    else:
        print("Estas fuera del limite")
        return posicion
def pos_izquierda(posicion):
    limite=0
    posicion_nueva=posicion-1
    if posicion_nueva>=limite:
        posicion=posicion_nueva
        return posicion
    else:
        print("Estas fuera del limite")
        return posicion

def pos_arriba(posicion):
    limite=0
    posicion_nueva=posicion-1
    if posicion_nueva>=Slimite:
        posicion=posicion_nueva
        return posicion
    else:
        print("Estas fuera del limite")
        return posicion




posicion_x=posicion_inicial_robot_x()
posicion_y=posicion_inicial_robot_y()
print(posicion_x)
print(posicion_y)
while True:
    mov=input("¿A donde quieres ir? (L/R/U/D) : ")

    if mov=="R":
        posicion_y=pos_derecha(posicion_y)
        print(posicion_x,posicion_y)
        continue
    if mov=="L":
        posicion_y=pos_izquierda(posicion_y)
        print(posicion_x,posicion_y) 
        continue

    if mov=="D":
        posicion_x=pos_abajo(posicion_x)
        print(posicion_x, posicion_y) 
        continue

    if mov=="U":
        posicion_x=pos_arriba(posicion_x)
        print(posicion_, posicion_y) 
        continue