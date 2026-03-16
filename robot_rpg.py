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
		indice_2 = 0
		encontrada = False
		while indice_2 < len(prohibidas): 
		# Comprueba que no haya repetidos en la lista de bloqueos
		# No esta la meta al lado
			if casilla == prohibidas[indice_2]:
				encontrada = True
				break
			indice_2 += 1
		if not encontrada:
			prohibidas.append(casilla)
		indice += 1
	return prohibidas

def agregar_adyacentes_meta(prohibidas, meta):
	adyacentes_meta = bloqueos_prohibidos(meta)
	indice_3 = 0
	while indice_3 < len(adyacentes_meta):
		casilla = adyacentes_meta[indice_3]
		indice_4 = 0
		encontrada = False
		while indice_4 < len(prohibidas):
			if casilla == prohibidas[indice_4]:
				encontrada = True
				break
			indice_4 += 1
		if not encontrada:
			prohibidas.append(casilla)
		indice_3 += 1
	return prohibidas

def generar_un_bloqueo(prohibidas, bloqueos_existentes):
    while True:
        nuevo = (random.randint(0, 9), random.randint(0, 9))
        indice_5 = 0
        en_prohibidas = False
        while indice_5 < len(prohibidas):
            if nuevo == prohibidas[indice_5]:
                en_prohibidas = True
                break
            indice_5 += 1
        indice_6 = 0
        en_bloqueos = False
        while indice_6 < len(bloqueos_existentes):
        	# Comprueba que no sean repetidas
            if nuevo == bloqueos_existentes[indice_6]:
                en_bloqueos = True
                break
            indice_6 += 1
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
    limite=9
    posicion_nueva=posicion+1
    if posicion_nueva == 
    elif posicion_nueva<=limite:
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
    if posicion_nueva>=limite:
        posicion=posicion_nueva
        return posicion
    else:
        print("Estas fuera del limite")
        return posicion

posiciones = posicion_inicial_robot()
posicion_x= posiciones[0]
posicion_y=posiciones[0]
print(posicion_inicial_robot())

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

intentos = 0

#if iniciar():
#	while not comprobacion_posicion():




#if intentos == 0:

#else:
#	print("LLEGASTE!!!!!!")

# Hacer el inicio del juego (def)
print("=====================")
print("TU objetivo es llegar a la meta")
print("Durante tu ruta habran casillas bloqueos")
# Correr el juego
# Hacer los mensajes al jugador
# Pistas
        continue
