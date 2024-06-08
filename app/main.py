import sys
import os

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        cmd = input()
        responseHandler(cmd)

def responseHandler(incoming):
    cmd = incoming.split(" ")
    output = ""

    if cmd[0] == "echo":
        output = " ".join(cmd[1:]) + "\n"
    elif cmd[0] == "type":
        commands = ["echo","type","exit"]
        if cmd[1] in commands:
            output = f"{cmd[1]} is a shell builtin\n"
        else:
            PATH = str(os.environ.get("PATH"))
            paths = PATH.split(": ")
            print(PATH)
            print(paths)
            for path in paths:
                print(f"{path}/{cmd[1]}")
                if os.path.isfile(f"{path}/{cmd[1]}"):
                    output = f"{cmd[1]} is {path}/{cmd[1]}\n"
            if output == "":
                output = f"{cmd[1]}: not found\n"
    elif cmd[0] == "exit" and cmd[1] == "0":
        status = 0
        sys.exit(status)
    else:
        output = f"{cmd[0]}: command not found\n"

    sys.stdout.write(output)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
