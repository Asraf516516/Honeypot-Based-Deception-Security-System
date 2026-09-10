import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 2222
LOG_FILE = "honeypot.log"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print("=== Honeypot-Based Deception Security System ===")
print(f"Honeypot listening on port {PORT}")
print("Waiting for suspicious connections...")

try:
    while True:
        client, address = server.accept()

        ip, port = address
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"{timestamp} | Connection from {ip}:{port}"

        print("\n[ALERT] Suspicious connection detected!")
        print(log_entry)

        with open(LOG_FILE, "a") as file:
            file.write(log_entry + "\n")

        client.sendall(
            b"Fake Service - Unauthorized access detected.\n"
        )

        client.close()

except KeyboardInterrupt:
    print("\nHoneypot stopped.")

finally:
    server.close()
