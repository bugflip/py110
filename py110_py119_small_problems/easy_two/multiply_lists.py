
def multiply_list(lst_one, lst_two):
    index = 0
    final = []
    while index < len(lst_one):
        final.append((lst_one[index] * lst_two[index]))
        index += 1
    return final