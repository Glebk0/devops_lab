def create_dict(names, professions):
    dictionary = {}
    i = 0
    for key in names:
        value = None
        if i < len(professions):
            value = professions[i]

        dictionary[key] = value
        i = i + 1
    return dictionary


def main():
    names = input("Enter names of employees separated by spaces: ").split()
    professions = input("Enter list of professions separated by spaces: ").split()
    dictionary = create_dict(names, professions)
    print(dictionary)


if __name__ == "__main__":
    main()
