def string_to_integer(given_string):
    results = 0
    for char in given_string:
        current_integer = ord(char) - ord('0')
        results = results * 10 +current_integer
    return results