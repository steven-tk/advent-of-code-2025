# https://adventofcode.com/2025/day/1

import sys



def load_file(argument):
    file_contents = []
    with open(argument) as f:
            file_contents = f.read()
    return file_contents



def load_dial():
    reset_dial =[]
    # add 0-99
    for i in range(0,100):
        reset_dial.append(i)
    # rotate to 50
    return reset_dial[50:] + reset_dial[:50]


# lol
# forgot to account for n > 100

def dial_calc(input):
    zero_tracker = 0
    rotations = load_file(input).split()
    dial = load_dial()
    print(f"The dial was reset to {dial[0]}.")
    print("Cracking safe...")

    for rotation in rotations:
        if rotation[0] == "L":
            dial = dial[-int(rotation[1:]):] + dial[:-int(rotation[1:])]
            print(f"Rotating by {rotation} turned the dial to {dial[0]}")
            if dial[0] == 0:
                zero_tracker += 1
        if rotation[0] == "R":
            dial = dial[int(rotation[1:]):] + dial[:int(rotation[1:])]
            print(f"Rotating by {rotation} turned the dial to {dial[0]}")
            if dial[0] == 0:
                zero_tracker += 1
    
    print(f"The dial stopped at zero {zero_tracker} times.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <run/test>")
        sys.exit(1)
    else:
        if sys.argv[1] == "run":
            return dial_calc("./rotations.txt")
        elif sys.argv[1] == "test":
            return dial_calc("./test.txt")
        else:
            print("Usage: python3 main.py <run/test>")
            sys.exit(1)
        



main()

