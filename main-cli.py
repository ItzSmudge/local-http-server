import http.server
import socket
import socketserver
import pyperclip
import os

print("\n"+"="*20)
print("Http Server - Local")
print("="*20,"\n")

path = os.environ['USERPROFILE'] + "\server"
path_exists = os.path.exists(path)

if not path_exists:
    os.mkdir(path)
    print("\nRoot folder file created.\nRoot path:", path)

port = 443
root = os.path.join(os.path.join(os.environ['USERPROFILE']), 'server')
os.chdir(root)

request = http.server.SimpleHTTPRequestHandler

hostname = socket.gethostname()

address = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address.connect(("8.8.8.8", 80))
ip = "http://" + address.getsockname()[0] + ":" + str(port)
pyperclip.copy(ip)

try:
    with socketserver.TCPServer(("", port), request) as http:
        print("\nRoot:", root)
        print("\nServer IP address: ", ip)
        print("...being hosted on port", port,"\n")
        print("IP address copied to clipboard\n")
        print("Scan QR code below to use on other devices:\n")
        command = "curl qrenco.de/" + ip
        os.system(command)
        print("\nlogs\n")
        http.serve_forever()
except KeyboardInterrupt or ConnectionResetError:
    pass