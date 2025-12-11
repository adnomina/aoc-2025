import sys

filename = ""

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    quit()


def turn_dial(start=50):
    dial = start
    password = 0

    with open(filename) as file:
        for line in file:
            direction = line[0]
            steps = int(line[1:])
            rollover = 0

            if direction == "L":
                if dial == 0:
                    rollover = steps // 100
                else:
                    rollover = (steps - dial - 1) // 100 + 1

                steps *= -1
            elif direction == "R":
                rollover = (dial + steps) // 100

            dial = (dial + steps) % 100
            password += rollover

            if direction == "L" and dial == 0:
                password += 1
 
    return password


if __name__ == "__main__":
    password = turn_dial()
    print(f"[result] Final password: {password}")
