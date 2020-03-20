#!/usr/bin/env python3
import argparse
import os
import time
from libs.add_servers import checking
from libs.list_servers import listar
from libs.send_commands import sender

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--servers", type=str, nargs='+', help='Ruta relativa del fichero que contendrá los '
                                                              'servidores. Si no existe, se creará de forma '
                                                              'automática.')
parser.add_argument("-i", "--indice", type=str, nargs='+', help='Ruta relativa del fichero que contendrá las '
                                                                'contraseñas cifradas. Si no existe, se creará de '
                                                                'forma automática.')
args = parser.parse_args()

ruta = args.servers[0]
indice = args.indice[0]


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
            checking.add_server(ruta, indice)
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
    if checking.checkServers(ruta, indice):
        if checking.checkIndice(indice, ruta):
            menu(ruta)


if __name__ == '__main__':
    comprobarFichero()
