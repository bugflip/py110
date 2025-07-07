def round_up(given_number):
    if given_number % 1 > 0:
        return int(given_number) + 1
    return int(given_number)

def halvsies(given_list):
    final_list = []
    half_rounded = round_up(len(given_list) / 2)
    final_list.append(given_list[0:half_rounded])
    final_list.append(given_list[half_rounded:])
    return final_list