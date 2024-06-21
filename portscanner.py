import socket
import sys
from datetime import datetime

#BANNER
print("__________              __      _________                                         ")
print("\______   \____________/  |_   /   _____/____ _____    ____   ____   ___________  ")
print("|     ___/  _ \_  __ \   __\  \_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __ \ ")
print("|    |  (  <_> )  | \/|  |    /        \  \___ / __ \|   |  \   |  \  ___/|  | \/ ")
print("|____|   \____/|__|   |__|   /_______  /\___  >____  /___|  /___|  /\___  >__|    ")
print("__________________________________________________________________________________")

#INPUT
while True:
    ip = input("\nGive me an IP address to scan: ")
    #IP_INPUT_CHECK
    def validate_ip_address(ip):
        parts = ip.split(".")
        if len(parts) != 4:
            print("Syntax Error: Invalid IP address format")
            return False
        for part in parts:
            if not part.isdigit():
                print("Syntax Error: Invalid IP address format")
                return False
            if int(part) < 0 or int(part) > 255:
                print("Syntax Error: Invalid IP address format")
                return False
        return True

    if validate_ip_address(ip):
        print("Valid IP address.")
        break
    else:
        print("Please try again.")

print("-" * 50)
print(f"Scanning target: {ip}")
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port number {port} is open.")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
