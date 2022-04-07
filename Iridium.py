import time
#import board
#from adafruit_rockblock import RockBlock

#uart = board.UART()
#uart.baudrate = 19200
#rb = RockBlock(uart)

def send_message(text_out = "hello world"):
    rb.text_out = text_out
    status = rb.satellite_transfer()
    retry = 0
    while status[0] > 8:
        time.sleep(10)
        status = rb.satellite_transfer()
        print(retry, status)
        retry += 1
    

def receive_message():
    #function
    status = rb.satellite_transfer()
    retry = 0
    while status[0] > 8:
        time.sleep()
        status = rb.satellite_transfer()
        print(retry, status)
        retry += 1
    print("\nDONE.")
    data = rb.data_in
    return data

def process_message():
    message = receive_message()

def main():
    main_function = 0
    print('hi')

main()
