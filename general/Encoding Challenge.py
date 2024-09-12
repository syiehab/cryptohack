from pwn import * # pip install pwntools
from Crypto.Util.number import bytes_to_long, long_to_bytes
import json
import base64
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

received = json_recv()
print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])

for i in range(100):
    encodeType = received["type"]
    encoded = received["encoded"]

    if encodeType == "hex":
        decoded = bytes.fromhex(encoded).decode("utf-8")
    elif encodeType == "base64":
        decoded = base64.b64decode(encoded).decode("utf-8")
    elif encodeType == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif encodeType == "bigint":
        decoded = long_to_bytes(int(encoded, 16)).decode("utf-8")
    elif encodeType == "utf-8":
        decoded = ''.join([chr(b) for b in encoded])

    to_send = {
        "decoded": decoded
    }

    json_send(to_send)

    print("Sent decoded value: ")
    print(decoded)

    received = json_recv()
    print("Response: ")
    print(received)
