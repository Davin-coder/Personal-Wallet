import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPresione Enter para continuar...")