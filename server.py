import socket
import json

IP = "localhost"
PORT = 7560
BUFFER = 1024
FORMAT = "utf-8"
ADDR = (IP, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDR)
webcams = []

while True:
    print("[STARTING SERVER...]")
    try:
        data, addr = sock.recvfrom(BUFFER)
    except ConnectionError:
        print("Connection reset by the client")
    try:
        json_data = json.loads(data)
    except (KeyError, TypeError):
        feedback = "invalid age data or missing age input. Please try filling out the field again"
        feedback = feedback.encode(FORMAT)
        sock.sendto(feedback, addr)

    print(f"[RECEIVED DATA] {json_data}")
    webcams.append(json_data)
    response_message = "the server received your data"
    response_message = response_message.encode(FORMAT)
    sock.sendto(response_message, addr)
    print(f"[CURRENT NUMBER OF WEBCAMS] {len(webcams)}")




