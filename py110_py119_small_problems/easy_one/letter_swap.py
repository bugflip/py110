
def swap_first_and_last_char(given_word):
    if len(given_word) > 1:
        return given_word[-1] + given_word[1:-1] + given_word[0]
    return given_word

def swap(given_string):
    return ' '.join([
        swap_first_and_last_char(word) for word in given_string.split()
        ])
