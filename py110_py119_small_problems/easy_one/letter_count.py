
def word_sizes(given_string):
    split_string = given_string.split()
    length_list = [len(''.join([
        char for char in word if char.isalpha()
            ]))
        for word in split_string
        ]
    final_dictionary = { 
        word_len:length_list.count(word_len)
        for word_len in length_list
        }
    return final_dictionary

