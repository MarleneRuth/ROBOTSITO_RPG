import random

def posicion_inicial_robot():
    return ((random.randint(0, 9)), (random.randint(0, 9)))

def posicion_meta():
    return (random.randint(0, 9), random.randint(0, 9))

def comprobacion_posicion(robot, meta):
    if robot == meta:
        return True
    return False

def adyacentes(posicion):
    x, y = posicion
    adyacentes = []
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    indice = 0
    while indice < len(movimientos):
        dx, dy = movimientos[indice]
        nueva_x = x + dx
        nueva_y = y + dy
        if 0 <= nueva_x <= 9 and 0 <= nueva_y <= 9:
            adyacentes.append((nueva_x, nueva_y))                   
        indice += 1
    return adyacentes

def casillas_prohibidas(robot, meta):
    prohibidas = []
    prohibidas.append(robot)
    prohibidas.append(meta)
    return prohibidas

def agregar_adyacentes_robot(prohibidas, robot):
    adyacentes_robot = adyacentes(robot)
    indice = 0
    while indice < len(adyacentes_robot):
        casilla = adyacentes_robot[indice]
        if casilla not in prohibidas:
            prohibidas.append(casilla)
        indice += 1
    return prohibidas

def agregar_adyacentes_meta(prohibidas, meta):
    adyacentes_meta = adyacentes(meta)
    indice_adyacentes = 0

    while indice_adyacentes < len(adyacentes_meta):
        casilla = adyacentes_meta[indice_adyacentes]

        if casilla not in prohibidas:
            prohibidas.append(casilla)
        indice_adyacentes += 1
    return prohibidas

def generar_bloqueos(prohibidas, bloqueos_existentes):
    while True:
        bloqueo_nuevo = (random.randint(0, 9), random.randint(0, 9))
        if bloqueo_nuevo not in prohibidas and bloqueo_nuevo not in bloqueos_existentes:
            return bloqueo_nuevo

def generar_todos_bloqueos(prohibidas, cantidad=10):
    bloqueos = []
    while len(bloqueos) < cantidad:
        nuevo_bloqueo = generar_bloqueos(prohibidas, bloqueos)
        bloqueos.append(nuevo_bloqueo)
    return bloqueos

def posicion_bloqueos(robot, meta, cantidad=10):
    prohibidas = casillas_prohibidas(robot, meta)
    prohibidas = agregar_adyacentes_robot(prohibidas, robot)
    prohibidas = agregar_adyacentes_meta(prohibidas, meta)
    bloqueos = generar_todos_bloqueos(prohibidas, cantidad)
    return bloqueos

def pos_derecha(posicion):
    posicion_nueva = posicion + 1
    if posicion_nueva <= 9:
        return posicion_nueva
    print("Estas fuera del limite")
    return posicion

def pos_izquierda(posicion):
    posicion_nueva = posicion - 1
    if posicion_nueva >= 0:
        return posicion_nueva
    print("Estas fuera del limite")
    return posicion

def pos_abajo(posicion):
    posicion_nueva = posicion + 1
    if posicion_nueva <= 9:
        return posicion_nueva
    print("Estas fuera del limite")
    return posicion

def pos_arriba(posicion):
    posicion_nueva = posicion - 1
    if posicion_nueva >= 0:
        return posicion_nueva
    print("Estas fuera del limite")
    return posicion

def pos_derecha_bloqueos(posicion):
    posicion_nueva = posicion - 1
    return posicion_nueva

def pos_izquierda_bloqueos(posicion):
    posicion_nueva = posicion + 1
    return posicion_nueva

def pos_abajo_bloqueos(posicion):
    posicion_nueva = posicion - 1
    return posicion_nueva

def pos_arriba_bloqueos(posicion):
    posicion_nueva = posicion + 1
    return posicion_nueva

def pista(robot, meta):
    x1, y1 = robot
    x2, y2 = meta 
    distancia = abs(x1 - x2)+abs(y1 - y2)
    if distancia<=2:
        print("Estas cerca...")
    elif distancia<=6:
        print("Estas a media distancia!")
    else:
        print("Estas lejos")


def verificar_power_up_repetido(prohibidas, power_ups):
    while True:
        casilla_power = (random.randint(0,9), random.randint(0,9))
        if casilla_power not in prohibidas and  casilla_power not in power_ups :
            return casilla_power
            
def generar_power_ups(prohibidas,cantidad=88):
    power_ups= []
    while len(power_ups)< cantidad:
        casilla_power = verificar_power_up_repetido(prohibidas,power_ups)
        power_ups.append(casilla_power)
    return power_ups


def generacion_de_mapa(robot, power_up, bloqueos):
    matriz = [
    [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9)], 
    [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9)],
    [(2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9)],
    [(3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9)],
    [(4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9)],
    [(5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9)],
    [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9)],
    [(7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9)],
    [(8,0), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9)],
    [(9,0), (9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9)]]
    for filas in matriz:
        contenido = 0
        for celda in filas:
            if celda not in bloqueos:
                if celda != robot:
                    if celda != power_up:
                        contenido = "⬜"
                    if celda in power_up:
                        contenido = "⚡"
                else:
                    contenido = "🤖"
            else:
                contenido = "🚫"
            print(contenido, end = "")
        print("\n")

def iniciar():
    robot = posicion_inicial_robot()
    meta = posicion_meta()
    bloqueos = posicion_bloqueos(robot, meta)
    posiciones_prohibidas = [robot, meta] + bloqueos
    power = generar_power_ups(posiciones_prohibidas)

    print("============================================")
    print("Tu objetivo es llegar a la meta")
    print("Durante tu ruta habran casillas bloqueos")
    print("Existe una casilla especial Power Up!")
    print("Si quieres una pista escribe H")
    print(f"Robot empieza en: {robot}")
    print("============================================")
    if robot == meta:
        return False

    return robot, meta, bloqueos, power

def main():
    intentos = 0
    robot, meta, bloqueos, power = iniciar()
    power_activo = False
    saltos = 1
    if robot and meta and bloqueos:
        while not comprobacion_posicion(robot, meta):
            generacion_de_mapa(robot, power, bloqueos)
            x, y = robot
            mov = input("¿A donde quieres ir? (W/A/S/D): ")

            if power_activo and mov !="H":
                saltos = 2
                power_activo = False
                power.remove(robot)
            else:
                saltos=1
            contador_saltos = 0
            if mov == "H":
                pista(robot, meta)
            while contador_saltos < saltos:
                if mov == "D":
                    y = pos_derecha(y)
                elif mov == "A":
                    y = pos_izquierda(y)
                elif mov == "S":
                    x = pos_abajo(x)
                elif mov == "W":
                    x = pos_arriba(x)
                elif mov == "H":
                    break
                else:
                    print("Movimiento Invalido")
                    if saltos == 2:
                        print("Perdiste tu power up 😂😂")
                    break
                robot = (x, y)
                contador_saltos += 1
            for indice in range(len(bloqueos)):
                if robot == bloqueos[indice]:
                    print("Casilla bloqueada")
                    if mov == "D":
                        y = pos_derecha_bloqueos(y)
                    elif mov == "A":
                        y = pos_izquierda_bloqueos(y)
                    elif mov == "S":
                        x = pos_abajo_bloqueos(x)
                    elif mov == "W":
                        x = pos_arriba_bloqueos(x)
                    robot = (x, y)
                    break
            if robot in power:
                print("Power up activado! ⚡⚡")
                power_activo = True

            for indice in range(len(bloqueos)):
                if robot == bloqueos[indice]:
                    print("Casilla bloqueada")
                    if mov == "D":
                        y = pos_derecha_bloqueos(y)
                    elif mov == "A":
                        y = pos_izquierda_bloqueos(y)
                    elif mov == "S":
                        x = pos_abajo_bloqueos(x)
                    elif mov == "W":
                        x = pos_arriba_bloqueos(x)

                    robot = (x, y)
                    break

            print(f"Posicion actual: {robot}")

        print("Llegaste a la meta upbino!!⚡")
        generacion_de_mapa(robot, power, bloqueos)

        print("Viva el tigre!!🐯")
main()
