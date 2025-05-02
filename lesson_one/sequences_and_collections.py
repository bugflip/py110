numbers = [1,2,3,4]
for i in range(len(numbers)):
        numbers[i] = numbers[i]+1

# print(numbers)

dict1 = {
    'apple': 'Produce',
    'carrot': 'Produce',
    'pear': 'Produce',
    'broccoli': 'Produce',
}
dict1['apple'] = 'Fruit'
dict1['carrot'] = 'Vegetable'

dict1['pear'] = 'Fruit'
dict1['broccoli'] = 'Vegetable'

# print(dict1)

del dict1['apple']

# print(dict1)

fruits = {'apple', 'banana', 'cherry'}
fruits.add('grape')
# print(fruits)
fruits.add('orange')
# print(fruits)
fruits.add('peach')
# print(fruits)

new_list = ['yo', 'this', 'is', 'sick']
# for index, word in enumerate(new_list):
    # print(f'the word {word} is at index {index}')

range_test = range(5, 50, 3)
# print(range_test.start)
# print(range_test.stop)
# print(range_test.step)