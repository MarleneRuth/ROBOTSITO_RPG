import random

def posicion_inicial_robot():
    robot = ((random.randint(0, 9)), (random.randint(0, 9)))
    return robot

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
    i = 0
    while i < len(adyacentes_robot):
        casilla = adyacentes_robot[i]
        j = 0
        encontrada = False
        while j < len(prohibidas):
            if casilla == prohibidas[j]:
                encontrada = True
                break
            j += 1
        if not encontrada:
            prohibidas.append(casilla)
        i += 1
    return prohibidas

def agregar_adyacentes_meta(prohibidas, meta):
    adyacentes_meta = bloqueos_prohibidos(meta)
    k = 0
    while k < len(adyacentes_meta):
        casilla = adyacentes_meta[k]
        l = 0
        encontrada = False
        while l < len(prohibidas):
            if casilla == prohibidas[l]:
                encontrada = True
                break
            l += 1
        if not encontrada:
            prohibidas.append(casilla)
        k += 1
    return prohibidas

def generar_un_bloqueo(prohibidas, bloqueos_existentes):
    while True:
        nuevo = (random.randint(0, 9), random.randint(0, 9))
        m = 0
        en_prohibidas = False
        while m < len(prohibidas):
            if nuevo == prohibidas[m]:
                en_prohibidas = True
                break
            m += 1
        n = 0
        en_bloqueos = False
        while n < len(bloqueos_existentes):
            if nuevo == bloqueos_existentes[n]:
                en_bloqueos = True
                break
            n += 1
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
    print("=====================")
    print("TU objetivo es llegar a la meta")
    print("Durante tu ruta habran casillas bloqueos")
    print(f"Robot empieza en: {robot}")
    
    if robot == meta:
        return False
    return robot, meta, bloqueos

def main():
    intentos = 0
    robot, meta, bloqueos = iniciar()
    if robot and meta and bloqueos:
        while not comprobacion_posicion(robot, meta):
            x, y = robot
            mov = input("¿A donde quieres ir? (L/R/U/D/H) : ")
            if mov == "R":
                y = pos_derecha(y)
            elif mov == "L":
                y = pos_izquierda(y)
            elif mov == "D":
                x = pos_abajo(x)
            elif mov == "U":
                x = pos_arriba(x)
            elif mov =="H":
                pista(robot, meta)
            else:
                print("Entrada invalida, usa solo L, R, U, D O H")
            robot = (x, y)
            print(f"Posicion actual: {robot}")

        print("Llegaste upbino!!")


main()
