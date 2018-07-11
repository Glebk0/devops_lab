def main():
    m = input("Enter first integers list separated by spaces: ").split()
    n = input("Enter second integers list separated by spaces: ").split()
    print("\n".join(sorted(list(set(m) ^ set(n)), key=int)))


if __name__ == "__main__":
    main()
