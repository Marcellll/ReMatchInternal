import socket
#Balance de production
#P - Imprimer le poids affiché (stable ou instable).
#IP - Imprimer immédiatement le poids affiché (stable ou instable).
#CP - Imprimer le poids en continu.
#SP - Imprimer le poids quand il est stable.
#Un espace est nécessaire dans chaque commande. Veuillez y prêter attention lors de la saisie des commandes.

# Scale configuration
SCALE_IP = '192.168.1.182'
SCALE_PORT = 9761  # Default port for Ohaus scales, check your manual

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the scale
    sock.connect((SCALE_IP, SCALE_PORT))
    print(f"Connected to scale at {SCALE_IP}:{SCALE_PORT}")

    # Send a command to request weight data
    # Refer to the i-DT33P manual for the correct command
    command = b"P\r\n"  # Example command, replace with the correct one
    sock.sendall(command)

    # Receive the response from the scale
    response = sock.recv(1024)
    print(f"Weight data: {response.decode('utf-8').strip()}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the socket
    sock.close()
    print("Connection closed")