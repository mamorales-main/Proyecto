#!/usr/bin/env python3

from libs.cifrar_pass import Crypt

import hashlib
import os
import random
import string
from itertools import islice

os.system('clear')


class remove_server:
    def servers(ruta, ip, user, port):
        lines = len(open(ruta, 'r').readlines())
        info_serv = ip + user + port
        with open(ruta, 'r') as server:
            cont = 1
            for linea in islice(server, 1, lines):
                datos = linea.split(',')
                servidor = datos[0] + datos[1] + datos[3].split('\n')[0]
                cont = cont + 1
                if servidor == info_serv:
                    with open(ruta, "r") as infile:
                        liness = infile.readlines()

                    with open(ruta, "w") as outfile:
                        pos = 0
                        for pos, line in enumerate(liness):
                            pos = pos + 1
                            if pos != cont:
                                outfile.write(line)
                    return servidor

    def indices(ruta, servidor):
        lines = len(open(ruta, 'r').readlines())
        encode = hashlib.md5(servidor.encode()).hexdigest()
        with open(ruta, 'r') as indice:
            cont = 1
            for linea in islice(indice, 1, lines):
                datos = linea.split(',')
                cont = cont + 1
                if encode == datos[0]:
                    with open(ruta, "r") as infile:
                        liness = infile.readlines()

                    with open(ruta, "w") as outfile:
                        pos = 0
                        for pos, line in enumerate(liness):
                            pos = pos + 1
                            if pos != cont:
                                outfile.write(line)
            return True

    def set(servers, indices):
        print('Introduce los datos del servidor a eliminar.')
        ip = input('IP/HOST: ')
        user = input('Usuario: ')
        port = input('Puerto: ')
        if remove_server.indices(indices, remove_server.servers(servers, ip, user, port)):
            print('\n¡Servidor eliminado con éxito!\n')
            input('Presiona cualquier tecla para continuar...')

        else:
            print('\nEl servidor introducido no es válido.\n')
            input('Presiona cualquier tecla para continuar...')
