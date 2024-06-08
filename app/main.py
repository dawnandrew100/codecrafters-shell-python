import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    cmds = input()
    responseHandler(cmds)

def responseHandler(incoming):
    cmds = incoming.split(" ")

    print(cmds)
    print(cmds[0])

if __name__ == "__main__":
    main()
