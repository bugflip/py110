# SET CONSTANTS
# SET DEGREE to \u00B0
# SET MINUTE to '
# SET SECOND to "\

# DEF get_whole_and_remainder
# 	GIVEN a float
# 	SET remainder to the remainder % 1
# 	SET whole_number to float minus remainder
# 	RETURN whole_number, remainder
	
# DEF get_next_float
# 	GIVEN a float
# 	RETURN float times 60

# DEF main_function
# 	GIVEN a float
# 	SET current_value to float
# 	SET storage to an empty list
# 	WHILE the length of storage is less than 3
# 		SET current_whole, current_remainder to get_whole_and_remainder(current_value)
# 		ADD current_whole to storage
# 		SET current_value to get_next_float(current_value)

DEGREE = "\u00B0"
MINUTE = "'"
SECOND = '\"'

def get_whole_and_remainder(given_float):
    remainder = given_float % 1
    whole_number = given_float - remainder
    return whole_number, remainder

def get_next_float(given_float):
    return given_float * 60

def digit_to_string(given_integer):
    if given_integer < 10:
        return '0' + str(given_integer)
    return str(given_integer)

def convert_list_to_string(given_list):
    string_list = [str(int(given_list[0]))]
    iterate_list = given_list[1:3]
    for value in iterate_list:
        string_list.append(digit_to_string(int(value)))
    return string_list

def dms(given_float):
    cur_value = given_float
    storage = []
    while len(storage) < 3:
        cur_whole, cur_remainder = get_whole_and_remainder(cur_value)
        storage.append(cur_whole)
        cur_value = get_next_float(cur_remainder)
    storage = convert_list_to_string(storage)
    return f'{storage[0]}{DEGREE}{storage[1]}{MINUTE}{storage[2]}{SECOND}'

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
