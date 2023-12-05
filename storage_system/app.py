import json


def save_data(data, filename: str) -> None:  # the filename should be a string and the function returns nothing
    try:
        with open(filename, "w") as file:  # write a new file, under filename
            json.dump(data, file)
    except Exception as e:
        print("There was an error saving the data")


def load_data(filename: str):
    try:
        with open(filename, "r") as file:  # read the file
            loaded_data = json.load(file)
            return loaded_data
    except Exception as e:
        print("There was an error loading the data")


# save_data([1, 2, 3, 4, 5], "list_of_numbers")
# save_data("this file just has a string", "string")
# save_data((2, "p", "l"), "tuple")
#
# load_data("list_of_numbers")
# load_data("string")
# load_data("tuple")
