import random

def posicion_inicial_robot():
    return ((random.randint(0, 9)), (random.randint(0, 9)))

def posicion_meta():
    return (random.randint(0, 9), random.randint(0, 9))

def comprobacion_posicion(robot, meta):
    if robot == meta:
        return True
    return False

def bloqueos_prohibidos(posicion):
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

def crear_lista_prohibidas(robot, meta):
    prohibidas = []
    prohibidas.append(robot)
    prohibidas.append(meta)
    return prohibidas

def agregar_adyacentes_robot(prohibidas, robot):
    adyacentes_robot = bloqueos_prohibidos(robot)
    indice = 0
    while indice < len(adyacentes_robot):
        casilla = adyacentes_robot[indice]
        indice_prohibidas = 0
        encontrada = False
        while indice_prohibidas < len(prohibidas):
            # Comprueba que no haya repetidos en la lista de bloqueos
            # No esta la meta al lado
            if casilla == prohibidas[indice_prohibidas]:
                encontrada = True
                break
            indice_prohibidas += 1
        if not encontrada:
            prohibidas.append(casilla)
        indice += 1
    return prohibidas

def agregar_adyacentes_meta(prohibidas, meta):
    adyacentes_meta = bloqueos_prohibidos(meta)
    indice_adyacentes = 0
    while indice_adyacentes < len(adyacentes_meta):
        casilla = adyacentes_meta[indice_adyacentes]
        indice_prohibidas = 0
        encontrada = False
        while indice_prohibidas < len(prohibidas):
            if casilla == prohibidas[indice_prohibidas]:
                encontrada = True
                break
            indice_prohibidas += 1
        if not encontrada:
            prohibidas.append(casilla)
        indice_adyacentes += 1
    return prohibidas

def generar_un_bloqueo(prohibidas, bloqueos_existentes):
    while True:
        nuevo = (random.randint(0, 9), random.randint(0, 9))
        indice_prohibidas = 0
        en_prohibidas = False
        while indice_prohibidas < len(prohibidas):
            if nuevo == prohibidas[indice_prohibidas]:
                en_prohibidas = True
                break
            indice_prohibidas += 1
        indice_bloqueos = 0
        en_bloqueos = False
        while indice_bloqueos < len(bloqueos_existentes):
            # Comprueba que no sean repetidas
            if nuevo == bloqueos_existentes[indice_bloqueos]:
                en_bloqueos = True
                break
            indice_bloqueos += 1
        if not en_prohibidas and not en_bloqueos:
            return nuevo

def generar_todos_bloqueos(prohibidas, cantidad=10):
    bloqueos = []
    while len(bloqueos) < cantidad:
        nuevo_bloqueo = generar_un_bloqueo(prohibidas, bloqueos)
        bloqueos.append(nuevo_bloqueo)
    return bloqueos

def posicion_bloqueos(robot, meta, cantidad=10):
    prohibidas = crear_lista_prohibidas(robot, meta)
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
    if distancia<=3:
        print("ESTAS MUY CERCA!")
    elif distancia<=6:
        print("ESTAS A MEDIA DISTANCIA!")
    else:
        print("Estas muy lejos")

def iniciar():
    robot = posicion_inicial_robot()
    meta = posicion_meta()
    bloqueos = posicion_bloqueos(robot, meta)
    print("============================================")
    print("TU objetivo es llegar a la meta")
    print("Durante tu ruta habran casillas bloqueos")
    print("Si quieres una pista escribe H")
    print(f"Robot empieza en: {robot}")
    print("============================================")
    
    if robot == meta:
        return False
    return robot, meta, bloqueos

def main():
    intentos = 0
    robot, meta, bloqueos = iniciar()
    bloqueos = posicion_bloqueos(robot, meta)
    if robot and meta and bloqueos:
        while not comprobacion_posicion(robot, meta):
            x, y = robot
            mov = input("¿A donde quieres ir? (A/D/W/S/H) : ")
            if mov == "D":
                y = pos_derecha(y)
            elif mov == "A":
                y = pos_izquierda(y)
            elif mov == "S":
                x = pos_abajo(x)
            elif mov == "W":
                x = pos_arriba(x)
            elif mov =="H":
                pista(robot, meta)
                continue
            else:
                print("Movimiento Invalido")
                continue
            robot = (x, y)
            indice_de_bloqueos = 0
            while indice_de_bloqueos < len(bloqueos):
                if robot == bloqueos[indice_de_bloqueos]:
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
                indice_de_bloqueos += 1
            print(f"Posicion actual: {robot}")
        print("Llegaste upbino!!")
        print("Viva el tigre!!")
main()
