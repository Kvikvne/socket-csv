# Socket to CSV Data Receiver

This Python application allows you to receive data from a client using a socket connection and save the received data to a CSV file. It provides a simple graphical user interface (GUI) for configuring the server's IP address and port, as well as starting and stopping the server.

## Prerequisites

Before running this application, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- The following Python libraries installed:
  - `socket`
  - `pandas`
  - `tkinter` (typically included in standard Python installations)
- Basic knowledge of socket programming.

## Getting Started

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory containing the `universal-robots-data-receiver.py` file.

3. Run the application using the following command:

   ```bash
   python universal-robots-data-receiver.py

## Usage

### Configuring the Server

1. Launch the application, and a GUI window will appear.

2. Configure the server's IP address and port in the respective input fields. By default, the IP address is set to `127.0.0.1` (localhost), and the port is set to `5000`.

### Starting the Server

1. Click the "Run" button to start the server. The server will start listening on the specified IP address and port.

2. The server will accept incoming connections and display a message when a client connects.

### Receiving Data

1. When a client connects, the server will receive data from the client and display it in the console.

2. The received data will be processed, cleaned, and added to a list.

3. The cleaned data will be saved to a CSV file with a filename in the format `YYYY-MM-DD_HH-MM-SS.csv`, where `YYYY-MM-DD_HH-MM-SS` represents the current date and time.

### Stopping the Server

1. To stop the server, click the "Stop" button. The server will stop accepting new connections.

2. Any existing connections will be closed gracefully, and the server will be stopped.

## Troubleshooting

- If you encounter any issues or errors while running the application, please check your Python environment and ensure that all required libraries are installed.

- Make sure that the client sending data to the server is configured to connect to the correct IP address and port.

- The application handles keyboard interrupts (e.g., pressing `Ctrl+C` in the terminal) to stop the server gracefully.

## License

This project is licensed under the MIT License .

## Acknowledgments

- This application was created as a basic example of socket programming in Python.

Feel free to modify and extend this application to suit your specific requirements.
