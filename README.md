# Python-Chat-App

This is a simple chat application written in Python. The program enables users to communicate over a local network in real-time by running in either **server** or **client** mode.

The application uses **sockets** for communication and **threading** to manage multiple connections simultaneously. It is designed to be lightweight, straightforward, and easy to set up, making it an ideal project for learning basic networking concepts.

## Features

1. **Server Mode**:
   - The server listens for incoming connections on a specified port.
   - It manages multiple clients simultaneously and broadcasts messages to all connected users.
2. **Client Mode**:
   - The client connects to the server via an IP address.
   - It allows real-time message exchange with other clients connected to the server.
3. **Multi-threading**:
   - Each client connection is handled in its own thread, ensuring smooth communication for all users.
4. **Cross-Platform**:
   - Works on any system supporting Python (e.g., Windows, Linux, macOS).

## Code Overview

### Key Functions:
1. **`get_local_ip()`**:
   - Detects and returns the local IP address of the machine running the script.
   - Defaults to `127.0.0.1` (localhost) if unable to determine the IP.

2. **`handle_client()`**:
   - Manages individual client connections on the server side.
   - Receives messages from a client and broadcasts them to all connected users.

3. **`broadcast()`**:
   - Sends a message to all connected clients.
   - Ensures messages are delivered reliably to every user in the chat.

4. **`run_server()`**:
   - Starts the server, listens for connections, and handles clients using threads.
   - Allows the server to send messages to all connected clients.

5. **`receive_messages()`**:
   - Runs on the client side to continuously listen for messages from the server.
   - Displays messages to the user in real-time.

6. **`run_client()`**:
   - Connects the client to the server and sends messages to the server.
   - Spawns a thread to receive incoming messages from the server.

7. **`main()`**:
   - Entry point of the program.
   - Guides the user to run the program as either a server or client.

## Requirements

- Python 3.x
- No external libraries required—relies on Python's built-in modules: `socket`, `threading`, and `sys`.

## How to Use

### Running the Server
1. Execute the script and select `1` when prompted to run as the server.
2. The server will start and display its local IP address.
3. Once started, the server will accept client connections and broadcast messages to all connected users.

### Running the Client
1. Execute the script and select `2` when prompted to run as the client.
2. Enter the server's IP address (e.g., `192.168.1.x`) to establish a connection.
3. Type messages to send them to the server, and you’ll see replies from other users in real-time.

### Exiting the Program
- Type `exit` to close the connection, both as a client or a server.

## Issues and Improvements

### Challenges Faced:
1. **Firewall Restrictions**:
   - When using different devices (e.g., laptop and phone), firewall settings initially blocked connections. This was resolved by adjusting the firewall to allow the program through.
2. **Message Display**:
   - When a user types a message, incoming messages from other users interrupt the typing experience. This makes the program less user-friendly during simultaneous communication.
3. **Port Variations**:
   - The server and client displayed different port numbers for the connection, causing some confusion during debugging.

### Potential Improvements:
1. **Better Input Handling**:
   - Implement non-blocking input for a seamless typing experience, even when new messages are received.
2. **Error Resilience**:
   - Add robust error handling for network-related issues like dropped connections or timeouts.
3. **Message Formatting**:
   - Clean up the terminal output to improve readability, ensuring user names and messages are displayed consistently.

## Future Enhancements

1. **Encryption**:
   - Introduce encryption (e.g., using SSL/TLS) to secure communication between the server and clients.
2. **File Sharing**:
   - Extend the functionality to support file transfers between users.
3. **Graphical Interface**:
   - Develop a GUI version using a library like `tkinter` or `PyQt` for a more modern user experience.

