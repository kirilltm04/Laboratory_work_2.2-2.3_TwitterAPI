"""
The program to navigate through any json file.
"""
import json
import sys


def file_reader(path: str) -> json:
    """
    The function to read the file and return a decoded json file
    :param path: str (path to json file)
    :return: decoded json
    (str -> json)
    """
    with open(path, "r", encoding="utf-8") as file_name:
        decoded_file = json.load(file_name)
        return decoded_file


def loop(path: str):
    """
    The function with the infinite loop to parse the decoded json file.
    :param path: str (path to json file)
    :return: parsed json file
    """
    data = file_reader(path)
    while True:
        if type(data) == dict:
            print(data.keys())
            print("\nEnter your key: ")
            key = input(">>> ")
            try:
                data = data[key]
            except KeyError or ValueError:
                print("\nWrong key!\n")
        elif type(data) == list:
            if len(data) != 0:
                for i in range(len(data)):
                    print(f"{i, data[i]}\n")
                print(f"It's a list. Choose the element of the list by its "
                      f"index named in the beginning (0 - {len(data)-1})")
                try:
                    num = int(input(">>> "))
                    if num in range(len(data)):
                        data = data[num]
                    else:
                        raise IndexError
                except ValueError:
                    print("\nWrong element index!")
                except IndexError:
                    print("\nWrong element index!")
            else:
                data = str(data)
        else:
            print(data)
            print("\nIt's the endpoint. If you want to return to the start, enter '..'")
            print("If you want to exit, enter any key")
            end = input(">>> ")
            if end == "..":
                loop(path)
            else:
                print("\nHope you had a nice experience!")
                sys.exit()


def main():
    """
    Main function which parses the path to file and calls the loop function.
    """
    try:
        print("Enter the path to file: ")
        file = str(input(">>> "))
        loop(file)
    except FileNotFoundError as err:
        print("\nWrong input!,", err)
        main()


if __name__ == "__main__":
    main()
