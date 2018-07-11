def main():
    avg = {}
    for _ in range(int(input("Enter number of students: "))):
        name, * \
            marks = input(
                "Enter student name and marks separated by space like "
                "'Ann 22 55 79': ").split()
        avg[name] = [float(i) for i in marks]
    marks = avg[input("Enter student name whose average mark is needed: ")]
    print("Average mark is", "%.2f" % (sum(marks) / len(marks)))
