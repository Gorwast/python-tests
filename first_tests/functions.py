
def say_hi():
    print("Hello User")


def if_statements(bool):
    if not bool:
        print("Hello World")
    else:
        print("Hi friend")

# 2D Lists


def number_grid():
    number_grid_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
    ]
    print(number_grid_list[0][2])


def translate(phrase, code_letter, replaced_letters):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + code_letter
        else:
            translation = translation + letter
    return translation


# Try Except test
def division_by_1():
    try:
        number = int(input("Enter a number: "))
        print(1 / number)
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print(err)


def archive_read(file_path):
    file_open = open(file_path, "r")
    print(file_open.readable())
    print(file_open.readline())
    file_line_list = file_open.readlines()
    file_open.close()
