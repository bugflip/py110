def string_to_integer(given_string):
    results = 0
    for char in given_string:
        current_integer = ord(char) - ord('0')
        results = results * 10 +current_integer
    return results

def correct_sign(first_char, given_integer):
    if first_char == '-':
        return given_integer * -1
    return given_integer

def string_to_signed_integer(given_string):
    first_value = given_string[0]
    if first_value in '+-':
        working_string = given_string[1:]
    else:
        working_string = given_string
    integer = string_to_integer(working_string)
    return correct_sign(first_value, integer)
