import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperar_tecla():
    input("⏸️  Presiona cualquier tecla para continuar...")
