#18. En el juego del tres en raya (gato) dos jugadores se turnan para colocar sus piezas, de una en una, sobre un tablero o matriz 3×3: Escribe un programa que pida dónde introducir la siguiente ficha, una X, comprobando que las coordenadas sean de una casilla vacía y que compruebe si dicha pieza introducida genera un tres en raya, bien sea horizontal, vertical, o diagonal.

tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
def imprimir_tablero():
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)
def colocar_ficha(jugador, fila, columna):
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador
        return True
    else:
        print("La casilla ya está ocupada. Intente de nuevo.")
        return False
def verificar_ganador(jugador):
    # Verificar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    # Verificar columnas
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False
print(imprimir_tablero())
