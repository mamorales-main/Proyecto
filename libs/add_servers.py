#!/usr/bin/env python3

from libs.cifrar_pass import Crypt

import hashlib
import os
import random
import string
from itertools import islice

os.system('clear')
cifrar = Crypt()


class checking:

    def checkServers(self, indice):
        try:
            with open(self, 'r') as fh:
                count = len(open(self).readlines())
                count2 = len(open(indice).readlines())
                if count != count2:
                    print('Para que el programa funcione, los dos ficheros deben coincidir')
                    exit(1)
                return True
        except FileNotFoundError:
            remove = input('El fichero de servidores introducido no existe, si desea continuar, el fichero de índices '
                           'se borrará/creará... (Y/N): ')
            if remove.capitalize() == 'Y':
                f = open(self, 'a+')
                f.write("host,user,pass,port\n")
                f.close()
                i = open(indice, 'w+')
                i.write("md5,passwd\n")
                i.close()
                return True
            else:
                exit(1)

    def checkIndice(self, ruta):
        try:
            with open(self, 'r') as fh:
                return True
        except FileNotFoundError:
            remove = input('El fichero de índices introducido no existe, si desea continuar, el fichero de servidores '
                           'se borrará/creará... (Y/N): ')
            if remove.capitalize() == 'Y':
                f = open(self, 'a+')
                f.write("md5,passwd\n")
                f.close()
                s = open(ruta, 'w+')
                s.write("host,user,pass,port\n")
                s.close()
                return True
            else:
                exit(1)

    def add_server(self, ruta):
        count = len(open(self).readlines())
        with open(self, 'r') as fh:
            check = ''
            os.system('clear')
            host = input('Ingrese la IP/HOST: ')
            user = input('Ingrese el usuario: ')
            passwd = input('Ingrese la contraseña: ')
            port = input('Ingrese el puerto, default [22]')
            if port == '':
                port = '22'
            linetop = str(host + user + port + '\n')
            for linea in islice(fh, 1, count-1):
                datos = linea.split(',')
                line = str(datos[0] + datos[1] + datos[3])
                if linetop == line:
                    print('Ya existe el servidor introducido')
                    check = line
                    self.add_server(fh)
            if check != linetop:
                x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                passwd = cifrar.encrypt(passwd, x)
                encode = hashlib.md5(str(host + user + port).encode()).hexdigest()
                file = open(ruta, 'a')
                file.write(encode + ',' + x + "\n")
                file.close()
                f = open(self, 'a')
                f.write(host + ',' + user + ',' + passwd + ',' + '' + port + "\n")
                f.close()
