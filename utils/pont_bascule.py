import socket
#Pont bascule
#XB - Imprime le poids brut sur requete
#SX - Réactivation de la transmission cyclique
#EX - Interruption de la transmission cyclique
#Un espace est nécessaire dans chaque commande. Veuillez y prêter attention lors de la saisie des commandes.
# Weight data: $    40340         0 kg 0200 - Stable output
# Weight data: $    20480         0 kg 0000 - Unstable output
# Scale configuration
SCALE_IP = '192.168.1.81'
SCALE_PORT = 2101  # Default port for Ohaus scales, check your manual

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the scale
    sock.connect((SCALE_IP, SCALE_PORT))
    print(f"Connected to scale at {SCALE_IP}:{SCALE_PORT}")

    # Send a command to request weight data
    #command = b"XB\r"  # Example command, replace with the correct one
    #sock.sendall(command)
    # Receive the response from the scale
    response = sock.recv(1024)
    print(f"Weight data: {response.decode('utf-8').strip()}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the socket
    sock.close()
    print("Connection closed")