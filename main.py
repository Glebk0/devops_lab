import task1
import task2
import task3
import task4
import task5
import task6


def main():
    task = input("Choose task to run. Type 'leave' to quit. Enter number: ")
    for pr in task:
        if task == "1":
            print("First task running")
            task1.main()
        elif task == "2":
            print("Second task running")
            task2.main()
        elif task == "3":
            print("Third task running")
            task3.main()
        elif task == "4":
            print("Fourth task running")
            task4.main()
        elif task == "5":
            print("Fifth task running")
            task5.main()
        elif task == "6":
            print("Sixth task running")
            task6.main()
        elif task == "leave":
            print("See you!")
            exit(0)
        else:
            print("Task number isn't correct! Enter correct number!")


if __name__ == "__main__":
    while True:
        main()
