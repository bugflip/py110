def union(list_one, list_two):
    return set(list_one + list_two)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True