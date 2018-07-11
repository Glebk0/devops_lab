def main():
    avg = {}
    for _ in range(int(input("Enter number of students: "))):
        name, *marks = input("Enter student name and marks separated by space: ").split()
        avg[name] = [float(i) for i in marks]
    marks = avg[input("Enter student name whose average mark is needed: ")]
    print("Average mark is", "%.2f" % (sum(marks) / len(marks)))


if __name__ == "__main__":
    main()
