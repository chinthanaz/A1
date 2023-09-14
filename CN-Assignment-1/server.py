#----------------------------------#
# SCS2205 Computer Networks I
# Take Home Assignment 1
#----------------------------------#

#----------------------------------#
# Name: C.A.Gamachchige
# Index Number: 20000561
#----------------------------------#

#----------------------------------#
# web server: This PC
# Client: Web browser
#----------------------------------#

# import socket module and sys module
import socket #which provides functions and classes for creating and interacting with network sockets.
import os     #which provides functions for working with files and directories
import subprocess # Import the subprocess module for executing external processes specifically the PHP interpreter

#Base directory for serving files
base = "htdocs"

#The phpObj function is used to generate a PHP array from a list of key-value pairs.
def phpObj(data):
    php_string = "$data = array(\n"
    
    # Check if data is empty or not a list
    if not data or not isinstance(data, list):
        return "$data = array();"

    for v in data:
        # Check if v has at least two elements
        if len(v) >= 2:
            php_string += f"    '{v[0]}' => '{v[1]}',\n"

    php_string += ");"
    return php_string


# Creating the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port
server_address = ("127.0.0.1", 2728)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening on http://127.0.0.1:2728")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    # Receive the client's request
    request = client_socket.recv(1024).decode("utf-8")

    # Extract the requested file path from the request
    try:
        file_path = request.split(" ")[1]
    except IndexError:
        file_path = "/"

    # Construct the full file path
    full_path = os.path.join(base, file_path.lstrip("/"))

    # Check if the file exists
    #This conditional statement checks two conditions
    # It checks whether the requested file exists in the server's file system. 
    # It checks whether the common path between the base directory (base) and the requested file's path (full_path) is equal to the base directory itself.
    if os.path.exists(full_path) and os.path.commonpath([base, full_path]) == base:
        
    #Checking If the Requested Resource Is a Directory
        if os.path.isdir(full_path):
            # check if there are specific index files like index.php or index.html within that directory.
            # If either of these index files exists, the code updates full_path to point to the index file,
            # effectively serving the index file as the default resource for that directory.
            if os.path.exists(os.path.join(full_path, "index.php")):
                full_path = os.path.join(full_path, "index.php")
            elif os.path.exists(os.path.join(full_path, "index.html")):
                full_path = os.path.join(full_path, "index.html")


            # Check if the requested resource is not a directory
        if not os.path.isdir(full_path):
            # Check if the requested file ends with ".php"
            if file_path.endswith(".php"):
                # Handle POST requests
                if request.startswith("POST"):
                    # Parse POST data
                    post_data = request.split("\r\n\r\n")[-1].split("&")
                    post_data = [item.split("=") for item in post_data]

                    # Create a PHP script with POST data
                    php_text = "<?php " + phpObj(post_data) + "\n $_POST = $data; ?> "

                    # Read the existing PHP code from the file
                    with open(full_path, 'r') as php_file:
                        php_code = php_file.read()

                    # Create a temporary PHP file with combined code
                    temp_file_location = "." + "temp" + "_" + os.path.basename(full_path)
                    with open(temp_file_location, 'w') as php_file:
                        php_file.write(php_text + php_code)

                    try:
                        # Execute the temporary PHP file
                        output = subprocess.run(['php', temp_file_location], capture_output=True, text=True, check=True)
                        response = f"HTTP/1.1 200 OK\r\n\r\n{output.stdout}"
                    except subprocess.CalledProcessError as e:
                        response = f"HTTP/1.1 500 Internal Server Error\r\n\r\nInternal Server Error\n{e.stderr}"

                    # Delete the temporary PHP file
                    if temp_file_location:
                        try:
                            os.remove(temp_file_location)
                            print(f"File '{temp_file_location}' has been deleted.")
                        except OSError as e:
                            print(f"Error deleting file: {e}")
                # Handle GET requests with parameters
                elif request.startswith("GET") and "?" in request:
                    # Extract GET parameters from the request
                    parameters = request.split("?")[1].split(" ")[0]
                    get_data = [item.split("=") for item in parameters.split("&")]

                    # Create a PHP script with GET data
                    php_text = "<?php " + phpObj(get_data) + "\n $_GET = $data; ?> "

                    # Read the existing PHP code from the file
                    with open(full_path, 'r') as php_file:
                        php_code = php_file.read()

                    # Create a temporary PHP file with combined code
                    temp_file_location = "." + "temp" + "_" + os.path.basename(full_path)
                    with open(temp_file_location, 'w') as php_file:
                        php_file.write(php_text + php_code)

                    try:
                        # Execute the temporary PHP file
                        output = subprocess.run(['php', temp_file_location], capture_output=True, text=True, check=True)
                        response = f"HTTP/1.1 200 OK\r\n\r\n{output.stdout}"
                    except subprocess.CalledProcessError as e:
                        response = f"HTTP/1.1 500 Internal Server Error\r\n\r\nInternal Server Error\n{e.stderr}"

                    # Delete the temporary PHP file
                    if temp_file_location:
                        try:
                            os.remove(temp_file_location)
                            print(f"File '{temp_file_location}' has been deleted.")
                        except OSError as e:
                            print(f"Error deleting file: {e}")
            else:
                # Serve non-PHP files
                with open(full_path, "rb") as file:
                    file_content = file.read()
                response = f"HTTP/1.1 200 OK\r\n\r\n{file_content.decode('utf-8')}"
        else:
            # Return a 404 response if the file does not exist
            response = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"


    # Send the response to the client
    client_socket.send(response.encode("utf-8"))

    # Close the client connection
    client_socket.close()
