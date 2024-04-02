import serial
import sys
import argparse

parser = argparse.ArgumentParser()

# Defining command line setup
def setup():
    parser.add_argument("-p", "--port", help="COM port name, ex: 'COM5'. Default=COM5. **Note: If port is specified, bitrate must also be specified.")
    parser.add_argument("-r", "--rate", help="COM port bitrate, ex: '9600'. Default=9600. **Note: If bitrate is specified, port must also be specified.")
    parser.add_argument("-f", "--filename", help="[String] Filename.")



""" A function that listens to the specified communication port (default is COM5 at a bitrate of 9600 bits/second)

:param name: The name of the output file.
:param serial_port: The serial port that we are listening to. 
:param bitrate: The bitrate of the serial port that we are listening to.

"""
def listen(name, serial_port="COM5", bitrate=9600):
    # Print the port, bitrate, and output filename.
    print(f"\033[95m[{serial_port}]\033[0m Listening at {bitrate} bit/sec. Writing to <{name}>")

    ser = serial.Serial(serial_port, bitrate)
    file = open(str(name), 'w')

    # Listen for 20 seconds (ish) and write the output to a file
    i = 0
    while True and i < 200:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            # print(data)
            file.write(f"{i},{data}\n")
            i += 1

    ## Close file writer and COM listener
    file.close()
    ser.close()


if __name__ == "__main__":
    setup()
    args = parser.parse_args()

    # Mode of operation: -b -r -f
    if args.port and args.rate and args.filename:
        listen(str(args.filename), serial_port=str(args.port), bitrate=int(args.rate) )
    elif args.filename: # Mode of operation: -f
        listen(str(args.filename))
    else: # Any other configuration is invalid
        print("Either no arguments were given or an invalid argument configuration was supplied, terminating...")
        sys.exit(1)
    

