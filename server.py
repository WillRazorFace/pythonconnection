import socket
import os


def send_file(socket: socket.socket, path: str) -> None:
    socket.sendall('upload'.encode())

    filename = os.path.basename(path)
    filesize = os.path.getsize(path)

    socket.sendall(f'{filename};{filesize}'.encode())

    with open(filename, 'rb') as file:
        data = file.read(filesize)
        socket.sendall(data)
        return


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind(('0.0.0.0', 2202))
    servidor.listen()

    print('Esperando conexões...')

    cliente, endereco = servidor.accept()

    with cliente:
        print(f'\nConectado com {endereco[0]} na porta {endereco[1]}\n')

        while True:
            try:
                command = input('>>> ')

                if not command:
                    continue

                if command == 'upload':
                    file_path = input('\t• Insert the file path >>> ')

                    if os.path.isfile(file_path):
                        send_file(cliente, file_path)
                        continue
                    else:
                        print('[-] Invalid path. [-]')
                        continue

                cliente.sendall(command.encode())

                saida = cliente.recv(1024).decode()

                if saida == 'continue':
                    continue

                print(f'\n{saida}\n')
            except KeyboardInterrupt:
                cliente.close()
                break
