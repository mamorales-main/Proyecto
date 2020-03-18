#!/usr/bin/env python3
import argparse
import os
import time
from libs.add_servers import checking
from libs.list_servers import listar
from libs.send_commands import sender

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, nargs='+', help='Ruta relativa del fichero. Si no existe, se creará de '
                                                              'forma automática.')
args = parser.parse_args()

ruta = args.file[0]


def menu(ruta):
    def print_menu():
        os.system('clear')
        print(30 * "-", "Administración de Servidores", 30 * "-")
        print("1. Listar servidores")
        print("2. Añadir servidores")
        print("3. Mandar comando/s")
        print("4. Menu Option 4")
        print("5. Exit")
        print(67 * "-")

    loop = True
    while loop:
        print_menu()
        choice = input("Introduce tu opción [1-5]: ")

        if choice == '1':
            os.system('clear')
            listar.servers(ruta)
        elif choice == '2':
            os.system('clear')
            checking.add_server(ruta)
        elif choice == '3':
            os.system('clear')
            command = input('Introduce un comando(Se enviará a todos los servidores disponibles): ')
            sender.send(ruta, command)
        elif choice == '4':
            print("Menu 4 has been selected")
        elif choice == '5':
            print("Menu 5 has been selected")
            loop = False
        elif choice == '':
            input("Selección incorrecta, porfavor presiona Enter o otra tecla para continuar..")
        else:
            input("Selección incorrecta, porfavor presiona Enter o otra tecla para continuar..")


def comprobarFichero():
    if checking.checkFile(ruta):
        menu(ruta)
    else:
        print('El fichero indicado no existe. Se procede con su creación...')


if __name__ == '__main__':
    comprobarFichero()
