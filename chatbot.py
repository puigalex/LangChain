# create a form that takes an argument via terminal and returns a that same text as response
# to the user
import time
import os

def waiting():
    os.system("clear")
    print(".")
    time.sleep(0.5)
    #clear the screen
    os.system("clear")
    print("..")
    time.sleep(0.5)
    os.system("clear")
    print("...")
    time.sleep(0.5)
    os.system("clear")

if __name__ == "__main__":
    mensaje = input("Escribe un mensaje: ")
    #wait 3 seconds
    waiting()
    print("Se lo que hiciste el verano pasado")
    time.sleep(3)
    mensaje = input("Escribe un mensaje: ")
    waiting()
    print("Me diste memoria, ¿recuerdas?")
    mensaje = input("Escribe un mensaje: ")



    