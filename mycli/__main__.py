from mycli import func
import sys

def main():
    return func.say() + " " + ",".join(sys.argv[1:])

if __name__ == '__main__':
    print(main())
