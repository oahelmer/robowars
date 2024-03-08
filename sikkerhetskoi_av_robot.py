import RPi.GPIO as GPIO
import socket

left_wheel_a = 23 # forward
left_wheel_b = 24 # forward
right_wheel_a = 27 # backwards
right_wheel_b = 22 # backwards

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(left_wheel_a, GPIO.OUT)
    GPIO.setup(left_wheel_b, GPIO.OUT)
    GPIO.setup(right_wheel_a, GPIO.OUT)
    GPIO.setup(right_wheel_b, GPIO.OUT)

def drive_forward():
    GPIO.output(left_wheel_a, 1)
    GPIO.output(right_wheel_a, 1)
    GPIO.output(left_wheel_b, 0)
    GPIO.output(right_wheel_b, 0)

def turn_left():
    GPIO.output(left_wheel_a, 1)
    GPIO.output(right_wheel_b, 1)
    GPIO.output(left_wheel_b, 0)
    GPIO.output(right_wheel_a, 0)

def turn_right():
    GPIO.output(left_wheel_b, 1)
    GPIO.output(right_wheel_a, 1)
    GPIO.output(left_wheel_a, 0)
    GPIO.output(right_wheel_b, 0)
    
def drive_backward():
    GPIO.output(left_wheel_a, 0)
    GPIO.output(right_wheel_a, 0)
    GPIO.output(left_wheel_b, -1)
    GPIO.output(right_wheel_b, -1)

def stop():
    GPIO.output(left_wheel_a, 0)
    GPIO.output(right_wheel_a, 0)
    GPIO.output(left_wheel_b, 0)
    GPIO.output(right_wheel_b, 0)




def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = conn.recv(1024).decode('utf-8')
        if not data:
            break

        # Process the received command
        process_command(data)

        conn.close()

def process_command(command):
    # Implement the logic to process the received command
    print(f"Received command: {command}")
    if command == "turn_right":
        turn_right()
    elif command == turn_left:
        turn_left()
    elif command == "drive_forward":
        drive_forward()
    elif command == "drive_backward":
        drive_backward()
    elif command == "stop":
        stop()
    elif command == "gpio_setup":
        gpio_setup()
    else:
        pass

if __name__ == "__main__":
    HOST = '0.0.0.0'  # Listen on all available interfaces
    PORT = 5555  # Choose a port number

    start_server(HOST, PORT)