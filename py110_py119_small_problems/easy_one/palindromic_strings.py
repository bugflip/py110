# Honestly didnt PEDAC this cause its very easy
def is_palindrome(given_string):
    return given_string == given_string[::-1]

## Part Two

# Didn't PEDAC this either because its simple but I probably should have

def is_real_palindrome(given_string):
    cleaned_string = ''.join(char for char in given_string if char.isalnum())
    return is_palindrome(cleaned_string.lower())

print(is_real_palindrome("he,llolleh."))