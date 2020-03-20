#!/usr/bin/env python3
from itertools import islice
import paramiko
from libs.cifrar_pass import Crypt
from libs.list_servers import listar
import hashlib


class sender:
    def send(ruta, indice, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        paramiko.util.log_to_file('../log_ssh')
        cifrar = Crypt()

        count = len(open(ruta).readlines())
        count2 = len(open(indice).readlines())
        with open(ruta, 'r') as fh:
            print(25 * '=' + ' Ejecutando comando/s en todos los servidores disponibles ' + 25 * '=')
            for linea in islice(fh, 1, count):
                array = []
                datos = linea.split(',')
                array = listar.server_on(datos[0], datos[1], int(datos[3].split('\n')[0]))
                pas = datos[2]
                if array:
                    with open(indice, 'r') as md:
                        for linea2 in islice(md, 1, count2):
                            encode = hashlib.md5(str(array[0] + array[1] + str(array[2])).encode()).hexdigest()
                            datosmd5 = linea2.split(',')
                            if datosmd5[0] == encode:
                                passwd = cifrar.decrypt(pas, datosmd5[1].split('\n')[0])
                                ssh.connect(array[0], username=array[1], password=passwd, port=array[2])
                                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                                print('Servidor: ' + array[0] + ':' + str(array[2]))
                                error = ssh_stderr.read()
                                if len(error) < 4:
                                    print('Ejecutado con éxito')
                                else:
                                    print('ERROR LOG:')
                                    print(error)
                                print('\n')
            print(107 * '=')
            input('Presiona ENTER para continuar...')
