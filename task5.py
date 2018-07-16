def main():
    path = input("Enter path. Only UDRL allowed:  ")
    path_switch(path)


def path_switch(path):
    path_int = 0
    for ch in path:
        if ch == "U":
            path_int += 2
        elif ch == "D":
            path_int -= 2
        elif ch == "R":
            path_int += 1
        elif ch == "L":
            path_int -= 1
        else:
            print("You wrote wrong path.")
            exit(1)
    if not path_int:
        print("Robot returned to starting point!")
    else:
        print("Robot is missing somewhere...")
