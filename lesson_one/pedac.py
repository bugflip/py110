def substrings(given_string):
    result = []
    start_index = 0
    while start_index <= len(given_string) - 2:
        end_index = start_index + 2
        while end_index <= len(given_string):
            substring = given_string[start_index:end_index]
            result.append(substring)
            end_index += 1
        start_index += 1
    return result

def is_palindrome(given_string):
	reversed_string = given_string[::-1]
	if given_string == reversed_string:
		return True
	else:
		return False
      

def palindrome_substrings(s):
    result = []
    substrings_list = substrings(s)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)

    return result

print(palindrome_substrings('safsdfsdnjcsdvbasjkdvhsdjvbsdfiuvsadviuaslaaloopooljdkafnsdjkfbwcicwned'))