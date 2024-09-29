first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (len(str_1[0]) - len(str_1[1])
                for str_1 in zip(first, second) if len(str_1[0]) != len(str_1[1]))
second_result = (len(first[index]) == len(second[index])
                 for index in range(len(first)))


print(list(first_result))
print(list(second_result))
