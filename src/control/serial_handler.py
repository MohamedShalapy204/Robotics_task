import serial
import time
import logging

class SerialHandler:
    def __init__(self, port: str, baud_rate: int):
        self.port = port
        self.baud_rate = baud_rate
        self.connection = None
        self.connected = False

    def connect(self):
        try:
            self.connection = serial.Serial(self.port, self.baud_rate, timeout=1)
            time.sleep(2)  # Wait for Arduino reset
            self.connected = True
            logging.info(f"Connected to Arduino on {self.port}")
        except Exception as e:
            logging.error(f"Failed to connect to serial port: {e}")
            self.connected = False

    def disconnect(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
            self.connected = False

    def send_command(self, cmd: str) -> str:
        if not self.connected:
            return "ERR NOT CONNECTED"
        self.connection.write((cmd + '\n').encode('utf-8'))
        response = self.connection.readline().decode('utf-8').strip()
        return response

    def move_to(self, x: float, y: float, z: float):
        return self.send_command(f"M {x} {y} {z}")

    def set_gripper(self, state: int):
        return self.send_command(f"G {state}")

    def home(self):
        return self.send_command("H")

    def emergency_stop(self):
        return self.send_command("E")
