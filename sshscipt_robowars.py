import os
from pynput import keyboard
from pynput.keyboard import Key

import socket

import socket
from pynput.keyboard import Key, Listener

def on_key_release(key):
    if key == Key.right:
        print("right")
        command_to_send = "turn_right"
        send_command(SERVER_HOST, SERVER_PORT, command_to_send)
        print("command sent")
    elif key == Key.left:
        print("left")
        command_to_send = "turn_left"
        send_command(SERVER_HOST, SERVER_PORT, command_to_send)
        print("command sent")
    elif key == Key.up:
        print("up")
        command_to_send = "drive_forward"
        send_command(SERVER_HOST, SERVER_PORT, command_to_send)
        print("command sent")
    elif key == Key.down:
        print("down")
        command_to_send = "drive_backward"
        send_command(SERVER_HOST, SERVER_PORT, command_to_send)
        print("command sent")
    elif key == Key.space:
        print("stop")
        command_to_send = "stop"
        send_command(SERVER_HOST, SERVER_PORT, command_to_send)
        print("command sent")
    elif key == Key.enter:
        print("setup")
        command_to_send = "gpio_setup"
        send_command(SERVER_HOST, SERVER_PORT, command_to_send)
        print("command sent")
    return None  # Return None for keys that don't have corresponding commands

def send_command(host, port, command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(command.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    SERVER_HOST = '192.168.1.131'  # Replace with the IP or hostname of the server
    SERVER_PORT = 5555  # Use the same port number as in the server script

    exit_program = False

    with Listener(on_release=on_key_release) as listener:
        listener.join()
        print("lol test")
        while not exit_program:
            print("test1")
            command_to_send = listener.join()
            print("test2")
#            if command_to_send is not None:
            print("sending command")
            send_command(SERVER_HOST, SERVER_PORT, command_to_send)
            print("command sent")