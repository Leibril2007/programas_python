# MODULOS
from programas.sumas import sumar2
from programas.restas import restar2
from vistas.menu import menu2
from vistas.lineas import cargar_lineas

# MODULOS DE PYTHON
from datetime import datetime
import time
import os 


try:
    while True:
        # Obtener la hora actual
        hora_actual = datetime.now().strftime('%H:%M:%S')

        # Limpiar la consola (opcional, dependiendo de si quieres limpiar todo o solo sobrescribir una línea)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Imprimir la hora
        print("Hora:", hora_actual)

        # Esperar 1 segundo
        time.sleep(1)

except KeyboardInterrupt:
    print("\n¡Hora detenida!")



# ---------USO DE OS------------------------

# Permite ejecutar comandos desde nuestro codigo
# os.system("ls")

programa = True
os.system("clear") # para que limpie la terminal cada vez que se ejecute


#------ MOSTRAR HORA EN ESTÁTICO ---------
# print("Hora",datetime.now().time())

#MOSTRAR HORA CON FORMATO DE HORA, MINUTO Y SEGUNDO ---------
# print("Hora",datetime.now().strftime('%H:%M:%S'))


while(programa):

    cargar_lineas(40)
    menu2()

    respuesta = int(input("[?] "))

    if respuesta == 1:
        print("Sumar dos números")
        sumar2()

    elif respuesta == 2:
        print("Resta de dos números")

        restar2()

    elif respuesta == 0:
        print("Salir del programa")
        programa = False
    
    os.system("clear")