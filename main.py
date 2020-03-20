#!/usr/bin/env python3
import argparse
import os
from libs.add_servers import checking
from libs.list_servers import listar
from libs.send_commands import sender
from libs.remove_servers import remove_server

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
        print("2. Añadir servidor")
        print("3. Mandar comando/s")
        print("4. Eliminar servidor")
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
            sender.send(ruta, indice, command)
        elif choice == '4':
            os.system('clear')
            remove_server.set(ruta, indice)
        elif choice == '5':
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
