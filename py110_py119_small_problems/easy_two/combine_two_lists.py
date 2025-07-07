def interleave(list_one, list_two):
    combined = list(zip(list_one, list_two))
    return [item for pair in combined for item in pair]
 