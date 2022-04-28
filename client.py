import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexao:
    conexao.connect(('localhost', 22))

    print('Conectado\n')

    endereco, porta = conexao.getpeername()

    while True:
        dados = input('>>> ')

        conexao.sendall(dados.encode())

        dados = conexao.recv(1024)

        print(f'\n({endereco}:{porta}) - {dados.decode()}\n')
