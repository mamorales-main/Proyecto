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

    def checkFile(self):
        check = ''
        try:
            with open(self, 'r') as fh:
                return True
        except FileNotFoundError:
            f = open(self, 'a')
            f.write("host,user,pass,port\n")
            f.close()
            return False

    def add_server(self):
        count = len(open(self).readlines())
        with open(self, 'r') as fh:
            x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
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
                passwd = cifrar.encrypt(passwd, x)
                encode = hashlib.md5(str(host + user + port).encode()).hexdigest()

                i = open('../indice.csv', 'a')
                i.write(encode + ',' + x + "\n")
                i.close()
                f = open(self, 'a')
                f.write(host + ',' + user + ',' + passwd + ',' + '' + port + "\n")
                f.close()
