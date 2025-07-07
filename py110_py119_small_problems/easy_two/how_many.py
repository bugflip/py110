

def get_occurances(lst):
    holder = {}
    for element in lst:
        holder[element] = holder.setdefault(element, 0) + 1
    return holder

def format_and_print(given_dict):
    for key, value in given_dict.items():
        print(f"{key} => {value}")

def count_occurrences(lst):
    format_and_print(get_occurances(lst))

