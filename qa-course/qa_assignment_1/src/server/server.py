import sys
import hashlib
import random
import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
DNS_ADDR = socket.gethostbyname(HOST)
PORT = int(str(sys.argv[len(sys.argv) - 1]))

serv.bind((DNS_ADDR, PORT))
serv.listen(5)

FILEPATH = "/serverdata/file"

ascii_lower = 'abcdefghijklmnopqrstuvwxyz'
ascii_upper = ascii_lower.upper()
digits= '0123456789'

def checksum(path):
    md5 = hashlib.md5()
    with open(path, "rb") as file_:
        content = file_.read()
        md5.update(content)
    return md5.hexdigest()

def create_file(path):
    ran = str(''.join(random.choices(ascii_lower + ascii_upper + digits, k = 1024)))
    with open(path, "w+") as file:
        file.write(ran)

create_file(FILEPATH)
digest = checksum(FILEPATH)

f = open(FILEPATH, "r")
data = f.read()

while True:
    connection, address = serv.accept()
    print(f"connection from {address}")
    connection.send("\nFile data:\n\n".encode("utf-8"))
    connection.send(data.encode("utf-8"))
    connection.send("\n\nChecksum:\n\n".encode("utf-8"))
    connection.send(digest.encode("utf-8"))
    f.close()