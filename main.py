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
            print("First task running \n")
            task1.main()
            main()
        elif task == "2":
            print("Second task running \n")
            task2.main()
            main()
        elif task == "3":
            print("Third task running ")
            task3.main()
            main()
        elif task == "4":
            print("Fourth task running \n")
            task4.main()
            main()
        elif task == "5":
            print("Fifth task running \n")
            task5.main()
            main()
        elif task == "6":
            print("Sixth task running \n")
            task6.main()
            main()
        elif task == "leave":
            print("See you!")
            exit(0)
        else:
            print("Task number isn't correct! Enter correct number!")
            main()


if __name__ == "__main__":
    main()