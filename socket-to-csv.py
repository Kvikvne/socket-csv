import socket
import pandas as pd
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import select
from PIL import Image, ImageTk


# Declare a global variable to keep track of the server status
server_running = False

# Create a global socket object
server_socket = None

def listen_to_socket(hostname, port):
    global server_socket
    current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    data_set = []
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((hostname, port))
        server_socket.listen(1)
        print(f"Listening on {hostname}:{port}")

        while server_running:  # Check the global variable to determine whether to continue running
            readable, _, _ = select.select([server_socket], [], [], 0.1)
            if server_socket in readable:
                client_socket, client_address = server_socket.accept()
                print(f"Connection established with {client_address}")

                data = client_socket.recv(1024)  # Receive data from the client
                if data:
                    received_data = data.decode("utf-8")
                    print(f"Received data: {received_data}")
                    
                    data_set.append(received_data)

                    response = "Data received and processed successfully!"
                    client_socket.send(response.encode("utf-8"))  # Send response to the client
                client_socket.close()
                cleaned_list = [item.strip() for item in data_set]
                print(cleaned_list)

                # Convert cleaned_list to a DataFrame and save as CSV
                df = pd.DataFrame({'Data': cleaned_list})
                csv_filename = f'{current_datetime}.csv'
                df.to_csv(csv_filename, index=False)
                print(f"CSV file '{csv_filename}' created.")

    except KeyboardInterrupt:
        print("Server stopped by user.")
    finally:
        server_socket.close()

# Callback function for the Run button
def run_button_callback():
    global server_running
    global server_socket

    if not server_running:
        hostname = ip_entry.get()
        port = int(port_entry.get())
        server_running = True
        runn_button.config(state="disabled")
        stop_button.config(state="normal")

        # Call the listen_to_socket function in a separate thread
        import threading
        server_thread = threading.Thread(target=listen_to_socket, args=(hostname, port))
        server_thread.start()

def stop_button_callback():
    global server_running
    global server_socket
    print('server stopped')
    server_running = False
    runn_button.config(state="normal")
    stop_button.config(state="disabled")

    # Close the server socket if it exists and the server is running
    if server_running and server_socket is not None:
        server_socket.close()
        server_socket = None  # Set to None to indicate that it's closed
        print('Server stopped')

# ---------------------------UI--------------------------------------------------------------
window = Tk()
window.title("Socket to CSV")
window.config(padx=20, pady=20, bg="white")


# IP Entry
ip_label = Label(text="IP:", bg="white", font=("Arial", 12))
ip_label.grid(row=1, column=0, sticky="E", padx=(0, 10))
ip_entry = Entry(width=20, font=("Arial", 12))
ip_entry.grid(row=1, column=1)
ip_entry.insert(0, "127.0.0.1")  # Default IP
ip_entry.focus()

# Port Entry
port_label = Label(text="Port:", bg="white", font=("Arial", 12))
port_label.grid(row=2, column=0, sticky="E", padx=(0, 10))
port_entry = Entry(width=20, font=("Arial", 12))
port_entry.grid(row=2, column=1)
port_entry.insert(0, "5000")  # Default port

# Run Button
runn_button = Button(text="Run", command=run_button_callback, font=("Arial", 14))
runn_button.grid(row=3, column=0, pady=(20, 0))

# Stop Button
stop_button = Button(text="Stop", command=stop_button_callback, font=("Arial", 14), state="disabled")
stop_button.grid(row=3, column=2, pady=(20, 0))

window.mainloop()