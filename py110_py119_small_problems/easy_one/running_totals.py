def running_total(given_list):
    final_list = []
    counter = 0
    for num in given_list:
        counter += num
        final_list.append(counter)
    return final_list


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True