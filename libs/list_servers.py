#!/usr/bin/env python3

import socket
import sys
import time
from itertools import islice


class listar:

    def server_on(ip, user, port):
        array = []
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            array.append(ip)
            array.append(user)
            array.append(port)
        sock.close()
        return array

    def servers(self):
        count = len(open(self).readlines())

        def portCheck(ip, port):
            abierto = "\x1b[6;30;42m ==ABIERTO== \x1b[0m"
            cerrado = "\x1b[6;30;41m ==CERRADO== \x1b[0m"
            puerto = str(ip + ':' + port.split('\n')[0])
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, int(port)))
                if result == 0:
                    print('|' + puerto.center(20, ' ') + '|' + 5 * ' ' + abierto + 5 * ' ' + '|')
                elif result == 11:
                    print('|' + puerto.center(20, ' ') + '|' + 5 * ' ' + cerrado + 5 * ' ' + '|')

                sock.shutdown(1)
                sock.close()
            except socket.gaierror:
                print('|' + puerto.center(20, ' ') + '|' + 5 * ' ' + cerrado + 5 * ' ' + '|')
            except socket.timeout:
                print('|' + puerto.center(20, ' ') + '|' + 5 * ' ' + cerrado + 5 * ' ' + '|')
            except socket.error:
                print('|' + puerto.center(20, ' ') + '|' + 5 * ' ' + cerrado + 5 * ' ' + '|')

        with open(self, 'r') as fh:
            print('|============================================|')
            print('|     SERVIDOR   ', '   |        STATUS         |')
            print('|'.ljust(21, ' ') + '|'.ljust(24, ' ') + '|')
            for linea in islice(fh, 1, count):
                datos = linea.split(',')
                portCheck(datos[0], datos[3])
            print('|============================================|')

        input('Presiona ENTER para continuar...')


"""with open('ssh_servers.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])"""
