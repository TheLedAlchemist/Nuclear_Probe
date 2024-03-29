import serial
import sys
import argparse

parser = argparse.ArgumentParser()

def setup():
    # Defining command line setup
    parser.add_argument("-p", "--port", help="COM port name, ex: 'COM5'. Default=COM5. **Note: If port is specified, bitrate must also be specified.")
    parser.add_argument("-r", "--rate", help="COM port bitrate, ex: '9600'. Default=9600. **Note: If bitrate is specified, port must also be specified.")
    parser.add_argument("-f", "--filename", help="[String] Filename.")



def listen(name, serial_port="COM5", bitrate=9600):
    print(f"\033[95m[{serial_port}]\033[0m Listening at {bitrate} bit/sec. Writing to <{name}>")

    ser = serial.Serial(serial_port, bitrate)

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(data)


if __name__ == "__main__":
    setup()
    args = parser.parse_args()

    if args.port and args.rate and args.filename:
        listen(str(args.filename), serial_port=str(args.port), bitrate=int(args.rate) )
    elif args.filename:
        listen(str(args.filename))
    else:
        print("Either no arguments or invalid argument configuration supplied, terminating...")
        sys.exit(1)
    

