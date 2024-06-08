import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    cmd = input()
    responseHandler(cmd)

def responseHandler(incoming):
    cmd = incoming.split(" ")
    output = ""

    if cmd[0] == "echo":
        output = "".join(cmd[1:])
    else:
        output = f"{cmd[0]}: command not found\n"

    sys.stdout.write(output)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
