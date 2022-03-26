import time
import board
from adafruit_rockblock import RockBlock

uart = board.UART()
uart.baudrate = 19200
rb = RockBlock(uart)

def send_message():
    #function
    message = "hello world"

def receive_message():
    #function
    message = "hello world"

def process_message():
    message = receive_message()

def main():
    main_function = 0
