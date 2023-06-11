import socket
import json
IP = "localhost"
PORT = 7560
BUFFER = 1024
FORMAT = "utf-8"
ADDR = (IP, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

webcam_dict = {
    "brand": None,
    "width": None,
    "height": None,
    "id": None
}

while True:
    webcam_dict["brand"] = input("enter a brand")
    try:
        webcam_dict["width"] = int(input("enter a width"))
        webcam_dict["height"] = int(input("enter a height"))
        webcam_dict["id"] = int(input("enter an id"))
    except ValueError:
        print("enter a valid integer")
    json_webcams = json.dumps(webcam_dict).encode(FORMAT)
    sock.sendto(json_webcams,ADDR)
    recv_data, addr = sock.recvfrom(BUFFER)
    recv_data.decode(FORMAT)
    print(recv_data)
    break
sock.close()





