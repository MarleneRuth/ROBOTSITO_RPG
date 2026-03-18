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

class RobotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Navigator 🤖")
        self.root.configure(bg="#1e1e2e")
        self._nueva_partida()
        self._build_ui()
        for tecla, mov in [("<w>","W"),("<a>","A"),("<s>","S"),("<d>","D"),("<h>","H")]:
            self.root.bind(tecla, lambda e, m=mov: self._mover(m))
            self.root.bind(tecla.upper(), lambda e, m=mov: self._mover(m))

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

    def _build_ui(self):
        tk.Label(self.root, text="🤖 Robot Navigator", bg="#1e1e2e",
                 fg="white", font=("Segoe UI", 14, "bold")).pack(pady=8)

        grid_f = tk.Frame(self.root, bg="#1e1e2e")
        grid_f.pack()
        self.celdas = {}
        for f in range(10):
            for c in range(10):
                lbl = tk.Label(grid_f, text="⬜", width=3, height=1,
                               font=("Segoe UI Emoji", 14), bg="#f8f9fa", relief="flat")
                lbl.grid(row=f, column=c, padx=1, pady=1)
                self.celdas[(f, c)] = lbl

        self.lbl_msg = tk.Label(self.root, text="Usa W A S D para moverte | H para pista",
                                bg="#1e1e2e", fg="#cdd6f4", font=("Segoe UI", 10))
        self.lbl_msg.pack(pady=6)

        btn_f = tk.Frame(self.root, bg="#1e1e2e")
        btn_f.pack(pady=4)
        tk.Button(btn_f, text="💡 Pista", width=8, font=("Segoe UI", 11, "bold"),
                  bg="#45475a", fg="white", relief="flat",
                  command=lambda: self._mover("H")).pack(side="left", padx=6)
        tk.Button(btn_f, text="🔄 Reiniciar", width=10, font=("Segoe UI", 11, "bold"),
                  bg="#1a73e8", fg="white", relief="flat",
                  command=self._reiniciar).pack(side="left", padx=6)

        self._dibujar()

    def _dibujar(self):
        for pos, lbl in self.celdas.items():
            if pos == self.robot:           lbl.config(text="🤖", bg="#1a73e8")
            elif pos in self.bloqueos:      lbl.config(text="🚫", bg="#ea4335")
            elif pos in self.power:         lbl.config(text="⚡", bg="#fbbc04")
            elif pos == self.meta and self.ganado: lbl.config(text="🏁", bg="#34a853")
            else:                           lbl.config(text="⬜", bg="#f8f9fa")

    def _mover(self, mov):
        if self.ganado: return

        if mov == "H":
            self.lbl_msg.config(text=pista(self.robot, self.meta)); return

        if self.power_activo:
            self.saltos = 2
            self.power_activo = False
        else:
            self.saltos = 1

        x, y = self.robot
        for _ in range(self.saltos):
            if   mov == "D": y = pos_derecha(y)
            elif mov == "A": y = pos_izquierda(y)
            elif mov == "S": x = pos_abajo(x)
            elif mov == "W": x = pos_arriba(x)
        self.robot = (x, y)

        # Primera verificación de bloqueo
        for i in range(len(self.bloqueos)):
            if self.robot == self.bloqueos[i]:
                self.lbl_msg.config(text="🚫 Casilla bloqueada!")
                if   mov == "D": y = pos_derecha_bloqueos(y)
                elif mov == "A": y = pos_izquierda_bloqueos(y)
                elif mov == "S": x = pos_abajo_bloqueos(x)
                elif mov == "W": x = pos_arriba_bloqueos(x)
                self.robot = (x, y); break

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
                self.robot = (x, y); break

        self._dibujar()

        if comprobacion_posicion(self.robot, self.meta):
            self.ganado = True
            self._dibujar()
            self.lbl_msg.config(text="🎉 Llegaste a la meta upbino! Viva el tigre! 🐯")

    def _reiniciar(self):
        self._nueva_partida()
        self._dibujar()
        self.lbl_msg.config(text="Usa W A S D para moverte | H para pista")


root = tk.Tk()
RobotGUI(root)
root.mainloop()
