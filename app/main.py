import sys
import threading


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        cmd = input()
        t = threading.Thread(target=lambda: responseHandler(cmd))
        t.start()

def responseHandler(incoming):
    cmd = incoming.split(" ")
    output = ""

    if cmd[0] == "echo":
        output = "".join(cmd[1:])
    elif cmd[0] == "exit" and cmd[1] == "0":
        return 0 
    else:
        output = f"{cmd[0]}: command not found\n"

    sys.stdout.write(output)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
