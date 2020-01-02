import socket
import sys
import random
import time
from datetime import datetime, timedelta

try:
    port = int(sys.argv[1])
except Exception:
    port = 3303

try:
    host = str(sys.argv[2])
except Exception:
    host = "localhost"


server_address = (host, port)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)

print('starting up on {} port {}'.format(*server_address))

# Listen for incoming connections
sock.listen(1)
connection_id = 0


def ask_for_password(connection):
    connection.sendall(
        "Tell me password to your class user in your VM\n".encode())
    connection.sendall("So we know this is not a robot\n".encode())


try:
    while True:
        # Wait for a connection
        print('Waiting for a connection...\n')
        connection, client_address = sock.accept()
        connection_id += 1
        connection_log_data = []
        try:
            loop = random.randint(2, 8)

            print(connection_id, ' -> new connection from: ', client_address)
            connection_log_data.append(
                'Timestamp: "' + str(
                    datetime.now() + timedelta(hours=5)) + '":\n')
            connection_log_data.append(
                'Connection with: "' + str(client_address) + '":\n')
            connection_log_data.append(
                'I will ask them ' + str(loop) + ' times for a password\n')

            ask_for_password(connection)
            for i in range(loop):
                if i != 0:
                    connection.sendall(
                        "Haha, you will not fool us. This password does not "
                        "work. Try again\n".encode())

                data = connection.recv(50)

                connection_log_data.append(
                    "Iteration " + str(i) + " response:")
                if data:
                    connection_log_data.append(data.decode("utf-8"))
                else:
                    connection.log_data.append("no response :(\n")

            connection.sendall(
                "Oh, runtime error. Sorry (and thanks)\n".encode())
            connection_log_data.append("Communication ended successfully\n")

        except KeyboardInterrupt:
            print("wat")
            break  # So i can close socket and file

        except Exception as e:
            print("Exception occured: " + str(e))
            print("Probably they cancelled connection\n")

        finally:
            # Clean up the connection
            connection.close()

            if connection_log_data:
                with open("log.txt", "a", encoding="utf-8") as file:
                    for line in connection_log_data:
                        file.write(line)
                    file.write("\n\n\n")
        time.sleep(0.1)

finally:
    sock.close()
