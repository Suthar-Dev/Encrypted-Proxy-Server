import socket

def xor(input, key="encrypted"):
    output = []
    for i in range(len(input)):
        xor = chr(ord(input[i]) ^ ord(key[i % len(key)]))
        output.append(xor)

    encrypted_string = ''.join(output)

    return encrypted_string

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 4500  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        xor(message)
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        xor(data)
        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
