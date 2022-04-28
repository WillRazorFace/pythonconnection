import socket

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

                cliente.sendall(command.encode())

                saida = cliente.recv(1024).decode()

                if saida == 'continue':
                    continue

                print(f'\n{saida}\n')
            except KeyboardInterrupt:
                cliente.close()
                break
