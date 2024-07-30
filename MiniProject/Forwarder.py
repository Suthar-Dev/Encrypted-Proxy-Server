import socket

def xor(input, key="encrypted"):
    output = []
    for i in range(len(input)):
        xor = chr(ord(input[i]) ^ ord(key[i % len(key)]))
        output.append(xor)

    encrypted_string = ''.join(output)

    return encrypted_string

def forwarder():
    # get the hostname
    host = socket.gethostname()
    print(host)
    src_port = 4500  

    server_socket = socket.socket()  # get instance

    server_socket.bind((host, src_port))  # bind host address and port together
    
    dest_port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, dest_port))  # connect to the server

    # configuration of how many client the server can listen simultaneously
    server_socket.listen(5)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        xor(data)
        print("from connected user: " + str(data))
        message = data
        xor(message)
        client_socket.send(message.encode()) # forward data to the server
        
        response = client_socket.recv(1024).decode()  # receive response
        print("from connected server: " + str(response))
        conn.send(response.encode())  # send data to the client

    conn.close()  # close the connection
    client_socket.close()  # close the connection
    

if __name__ == '__main__':
    forwarder()
