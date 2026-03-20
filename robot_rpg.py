import random
import tkinter as tk

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
    return posicion

def pos_izquierda(posicion):
    posicion_nueva = posicion - 1
    if posicion_nueva >= 0:
        return posicion_nueva
    return posicion

def pos_abajo(posicion):
    posicion_nueva = posicion + 1
    if posicion_nueva <= 9:
        return posicion_nueva
    return posicion

def pos_arriba(posicion):
    posicion_nueva = posicion - 1
    if posicion_nueva >= 0:
        return posicion_nueva
    return posicion

def pos_derecha_bloqueos(posicion):
    return posicion - 1

def pos_izquierda_bloqueos(posicion):
    return posicion + 1

def pos_abajo_bloqueos(posicion):
    return posicion - 1

def pos_arriba_bloqueos(posicion):
    return posicion + 1

def pista(robot, meta):
    x1, y1 = robot
    x2, y2 = meta
    distancia = abs(x1 - x2) + abs(y1 - y2)
    if distancia <= 2:
        return "Estas cerca... 🟢"
    elif distancia <= 6:
        return "Estas a media distancia! 🟡"
    else:
        return "Estas lejos 🔴"

def verificar_power_up_repetido(prohibidas, power_ups):
    while True:
        casilla_power = (random.randint(0,9), random.randint(0,9))
        if casilla_power not in prohibidas and casilla_power not in power_ups:
            return casilla_power

def generar_power_ups(prohibidas, cantidad=4):
    power_ups = []
    while len(power_ups) < cantidad:
        casilla_power = verificar_power_up_repetido(prohibidas, power_ups)
        power_ups.append(casilla_power)
    return power_ups

# ── INTERFAZ TKINTER ──────────────────────────────────────────────

class RobotGUI: # Todo lo que este adentro sera un robotGUI, (Esta clase representa la ventana gráfica del juego y lo gestiona.)
    def __init__(self, root):#Es el constructor: se ejecuta automáticamente cuando creas un objeto RobotGUI. Recibe root, que es la ventana principal de Tkinter.
        self.root = root #self root guarda a la ventana del juego como unico
        self.root.title("Robotsito 🤖")
        self.root.configure(bg="#bc75e0")
        self._nueva_partida()#Inicia la partida
        self._build_ui()#Construye todos los elementos visuales botones , etc
        for tecla, mov in [("<w>","W"),("<a>","A"),("<s>","S"),("<d>","D"),("<h>","H")]:
            #son sintaxis de tkinter para teclas especiales, con bind (<>)Y CADA SE VINCULA SEGUN EL MOV QUE SEA 
            self.root.bind(tecla, lambda e, m=mov: self._mover(m))#e=evento
            self.root.bind(tecla.upper(), lambda e, m=mov: self._mover(m))# Lmbda es una "funcion" anonima y pequenia de un solo uso
#lambda permite hacer una funcion sin hacer una mas aparte
    def _nueva_partida(self):
        self.robot = posicion_inicial_robot()
        self.meta  = posicion_meta()
        while self.robot == self.meta:
            self.meta = posicion_meta()
        self.bloqueos     = posicion_bloqueos(self.robot, self.meta)
        prohibidas        = [self.robot, self.meta] + self.bloqueos
        self.power        = generar_power_ups(prohibidas)
        self.power_activo = False
        self.saltos       = 1
        self.ganado       = False
#Es lo mismo que hicimos en la terminal (ariiba)
    def _build_ui(self):#construye los widgets
        tk.Label(self.root, text="🤖 Robotsito", bg="#bc75e0", #color fondo letras
                 fg="white", font=("Segoe UI", 14, "bold")).pack(pady=8) # titulo y posicion en px de titulo

        grid_f = tk.Frame(self.root, bg="#1e1e2e") #color de los bordes de la matriz
        grid_f.pack() # visualiza las casillas
        self.celdas = {} #diccionario vacio y agregue las celdas x,y
        for f in range(10):
            for c in range(10):#lenguaje the thinker misma logica
                lbl = tk.Label(grid_f, text="⬜", width=3, height=1, #tamanio de las casillas en ancho y alto
                               font=("Segoe UI Emoji", 14), bg="#f8f9fa", relief="flat") #relief relieve
                lbl.grid(row=f, column=c, padx=1, pady=1) #Pady distancia de casillas
                self.celdas[(f, c)] = lbl #Guarda la referencia a ese Label con su posición como llave

        self.lbl_msg = tk.Label(self.root, text="Usa W A S D para moverte | H para pista",
                                bg="#bc75e0", fg="#000000", font=("Segoe UI", 10)) #fondo y letras
        self.lbl_msg.pack(pady=6) # distancia entre la matriz las letras y los botones

        btn_f = tk.Frame(self.root, bg="#bc75e0") #Caja de widgets = botonones,labels, etc
        btn_f.pack(pady=4 ) #visualiza los botones
        tk.Button(btn_f, text="💡 Pista", width=8, font=("Segoe UI", 11, "bold"),
                  bg="#280847", fg="white", relief="flat", # letras
                  command=lambda: self._mover("H")).pack(side="left", padx=6) #llama a la funcion de pistas, los botones no envian a eventos
        tk.Button(btn_f, text="🔄 Reiniciar", width=10, font=("Segoe UI", 11, "bold"),
                  bg="#0c1145", fg="white", relief="flat",
                  command=self._reiniciar).pack(side="left", padx=6)#Le dice a Tkinter dónde colocar un widget dentro de su contenedor, y es centrado por defecto

        self._dibujar()

    def _dibujar(self):
        for pos, lbl in self.celdas.items():#.items() te da cada TUPLA del diccionario:
            if pos == self.robot:           lbl.config(text="🤖", bg="#1a73e8")
            elif pos in self.bloqueos:      lbl.config(text="🚫", bg="#ea4335")
            elif pos in self.power:         lbl.config(text="⚡", bg="#fbbc04")
            elif pos == self.meta and self.ganado: lbl.config(text="🏁", bg="#34a853")
            else:                           lbl.config(text="⬜", bg="#f8f9fa")

    def _mover(self, mov):
        if self.ganado: return#SI SE CUMPLE NO HACE NADA MAS

        if mov == "H":
            self.lbl_msg.config(text=pista(self.robot, self.meta)); return #CONFIGURA EL MENSAJE PARA QUE SEA LA PISTA

        if self.power_activo:
            self.saltos = 2
            self.power_activo = False
        else:
            self.saltos = 1

        x, y = self.robot
        for _ in range(self.saltos): #no importa el numero de vueltas solo repite n veces
            if   mov == "D": y = pos_derecha(y) #+
            elif mov == "A": y = pos_izquierda(y)#-
            elif mov == "S": x = pos_abajo(x)#+
            elif mov == "W": x = pos_arriba(x)#-
        self.robot = (x, y)

        # Primera verificación de bloqueo
        for i in range(len(self.bloqueos)):
            if self.robot == self.bloqueos[i]:
                self.lbl_msg.config(text="🚫 Casilla bloqueada!") #cambia el mensaje
                if   mov == "D": y = pos_derecha_bloqueos(y) #-
                elif mov == "A": y = pos_izquierda_bloqueos(y)#+
                elif mov == "S": x = pos_abajo_bloqueos(x)#-
                elif mov == "W": x = pos_arriba_bloqueos(x)#+
                self.robot = (x, y)
                break

        if self.robot in self.power:
            self.power.remove(self.robot)
            self.lbl_msg.config(text="⚡ Power Up! Proximo movimiento x2")
            self.power_activo = True

        # Segunda verificación de bloqueo (igual que el original)
        for i in range(len(self.bloqueos)):
            if self.robot == self.bloqueos[i]:
                self.lbl_msg.config(text="🚫 Casilla bloqueada!")
                if   mov == "D": y = pos_derecha_bloqueos(y)
                elif mov == "A": y = pos_izquierda_bloqueos(y)
                elif mov == "S": x = pos_abajo_bloqueos(x)
                elif mov == "W": x = pos_arriba_bloqueos(x)
                self.robot = (x, y)
                break

        self._dibujar()# Dibuja el mapa con la nueva posicion del robot

        if comprobacion_posicion(self.robot, self.meta):
            self.ganado = True
            self._dibujar()
            self.lbl_msg.config(text="🎉 Llegaste a la meta upbino! Viva el tigre! 🐯")

    def _reiniciar(self):
        self._nueva_partida()
        self._dibujar()
        self.lbl_msg.config(text="Usa W A S D para moverte | H para pista")


root = tk.Tk()#Crea la ventana principal del gui
RobotGUI(root) #Inicia el objeto, todo (botones)
root.mainloop()#permite que el juego este activo mientras haya eventos
