def get_six_numbers():
    format_dict = { 
                    1: '1st',
                    2: '2nd',
                    3: '3rd',
                    4: '4th',
                    5: '5th',
                    6: 'last'
                }
    counter = 1
    list_of_inputs = []
    while counter < 7:
        current_input = input(f'Enter the {format_dict[counter]} number: ')
        while not check_if_number(current_input):
            current_input = input(f'Enter the {format_dict[counter]} number: ')
        list_of_inputs.append(current_input)
        counter += 1
    return list_of_inputs

def check_if_number(inp): # This is added after algorithm thinking in PEDAC
    if inp.isnumeric():
        return True
    print("Input must be a number!")
    return False

def get_and_display_result(search_number, search_list):
    display_list = ', '.join(search_list) #This is added after A in PEDAC
    if search_number in search_list:
        print(f'{search_number} is in {display_list}.')
    else:
        print(f"{search_number} isn't in {display_list}.")

def main_program():
    list_numbers = get_six_numbers()
    last_number = list_numbers.pop()
    get_and_display_result(last_number, list_numbers)

main_program()