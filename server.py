import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind(('0.0.0.0', 2202))
    servidor.listen()

    print('Esperando conexões...')

    cliente, endereco = servidor.accept()

    with cliente:
        print(f'\nConectado com {endereco[0]} na porta {endereco[1]}')

        while True:
            dados = cliente.recv(1024)

            print(f'\n({endereco[0]}:{endereco[1]}) - {dados.decode()}\n')

            dados = input('>>> ')

            cliente.sendall(dados.encode())
