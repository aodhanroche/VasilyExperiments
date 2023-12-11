from app import save_data, load_data

save_data([1, 2, 3, 4, 5], "list_of_numbers")
save_data("this file just has a string", "string")
save_data((2, "p", "l"), "tuple")

load_data("list_of_numbers")
load_data("string")
load_data("tuple")