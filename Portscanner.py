import socket
import time

# List of Ips and Websites names
host = ["Website1", "Ip1"]

# Change the starting / ending ports bassed on the needs
starting_port = 440
ending_port = 450

for i in range(len(host)):
    hosts = host[i]
    ip = socket.gethostbyname(hosts)
    print(f"Scanning open ports for {ip}\n")
    start = time.time()
    for i in range(starting_port, ending_port):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        timing = 0.2
        client.settimeout(timing)

        result = client.connect_ex((ip, i))
        if result == 0:
            print(f"Port {i} is open")
        client.close()

    print(f"Scan took {time.time() - start:.2f} seconds")
