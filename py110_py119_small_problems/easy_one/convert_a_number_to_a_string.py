def signed_integer_to_string(given_integer):
    if given_integer < 0:
        final_list = ['-']
        list_of_digits = isolate_digits_to_list_negative(given_integer)
    else:
        if given_integer == 0:
            final_list = []
        else:
            final_list = ['+']
        list_of_digits = isolate_digits_to_list_positive(given_integer)

    digit_char = '0123456789'
    for digit in list_of_digits:
        final_list.append(digit_char[digit])
    return ''.join(final_list)

def isolate_digits_to_list_positive(working_integer):
    final_list = []
    while True:
        working_integer, current_digit = divmod(working_integer, 10)
        final_list.append(current_digit)
        if working_integer == 0:
            break
    return final_list[::-1]

def isolate_digits_to_list_negative(working_integer):
    working_integer = -working_integer
    final_list = []
    while True:
        working_integer, current_digit = divmod(working_integer, 10)
        final_list.append(current_digit)
        if working_integer == 0:
            break
    return final_list[::-1]

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True