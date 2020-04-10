import socket
import sys
import argparse

# Initiating the argparse object or creating the parser
parser = argparse.ArgumentParser()

# Adding Positional Argument which are mandatory to run the script
parser.add_argument("server", help="Server Name to Connect")
parser.add_argument("port", help="Server Port Number You want to Connect")

# Parsing the Arguments
args = parser.parse_args()

server_name = args.server
server_port = args.port

print(f'Checking if Port {server_port} is open on Server {server_name}')

# Creating a Socket to Initiate the Communication with the Server
client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Check if the Specific Port on the Server is Open using connect_ex and see if the result is Zero for Successful Connection or Non-Zero for Failure.
result = client_soc.connect_ex((server_name, int(server_port)))

if result == 0:
    print(f'PASS : port {server_port} on server {server_name} is open')
    client_soc.close()
else:
    print(f'FAIL : port {server_port} on server {server_name} is closed')