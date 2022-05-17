def my_open(file_name):
    with open(file_name) as f:
        print(*f.readline().rstrip("\n").split(","), sep="\n")


if __name__ == "__main__":
    my_open("numbers.txt")
