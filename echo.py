import sys

def echo():
    shout = "--s" in sys.argv
    message = input("Say something please: ")
    print(message.upper() if shout else message)

if __name__ == "__main__":
    echo()