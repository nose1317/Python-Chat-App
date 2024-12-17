import socket
import threading
import sys

PORT = 59876

# Function to detect the local IP address of the machine
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))                             # Dummy IP just to get local IP
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'                                       # Default to localhost if unable to detect
    finally:
        s.close()
    return local_ip

# Function to handle communication with a client
def handle_client(client_socket, client_address, clients):
    print(f"New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print(f"Client {client_address} disconnected.")
                break
            print(f"\n{client_address}: {message}")  # Display received message
            # Broadcast received message to other clients
            broadcast(message, clients)
        except Exception as e:
            print(f"Error with client {client_address}: {e}")
            break
    client_socket.close()
    clients.remove(client_socket)

# Function to broadcast messages to all connected clients
def broadcast(message, clients):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            continue

# Main function to run the server
def run_server():
    local_ip = get_local_ip()
    print(f"Starting server on {local_ip}:{PORT}...")

    # Create and bind the socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('0.0.0.0', PORT))  # Listen on all network interfaces
    except OSError as e:
        print(f"Error binding to port {PORT}: {e}")
        return

    server_socket.listen(5)
    print(f"Server started and listening on {local_ip}:{PORT}")

    # List of connected clients
    clients = []

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            clients.append(client_socket)
            threading.Thread(target=handle_client, args=(client_socket, client_address, clients), daemon=True).start()

            # Server sends messages continuously
            while True:
                server_message = input(f"{local_ip}: ")
                if server_message.lower() == 'exit':
                    break
                # Send message with "Server:" prefix only in the broadcast
                broadcast(f"Server: {server_message}", clients)

        except Exception as e:
            print(f"Error accepting connections: {e}")
            break

    server_socket.close()

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"\n{message}")  # Print received message
        except:
            break

# Function to run the client
def run_client(server_ip, username):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_ip, PORT))
        print(f"Connected to server at {server_ip}:{PORT}")
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        return

    # Start a thread to receive messages
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input(f"{username}: ")
        if message.lower() == 'exit':
            break
        client_socket.send(f"{username}: {message}".encode())  # Send the message with the username

    client_socket.close()

# Main entry function
def main():
    print("Welcome to the Chat Program!")

    # Get the local IP of the machine
    local_ip = get_local_ip()
    print(f"Detected local IP: {local_ip}")

    # Ask for username input
    username = input("Enter your username: ")
    print(f"Hello, {username}!")

    # Ask if the user wants to be a client or a server, keep looping until valid input
    while True:
        choice = input("Do you want to run the server or the client? (Enter '1' for server or '2' for client): ").strip()
        if choice == '1':
            print(f"Starting server on {local_ip}:{PORT}...")
            run_server()
            break
        elif choice == '2':
            # Ask for server IP (could be the local machine or another machine)
            server_ip = input("Enter the server's IP address: ").strip()
            run_client(server_ip, username)
            break
        else:
            print("Invalid choice. Please enter '1' for server or '2' for client.")

if __name__ == "__main__":
    main()
