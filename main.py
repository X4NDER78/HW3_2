# HW3
# 1 Зформуйте строку, яка містить певну інформацію про символ в відомому слові. Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'". Слово та номер отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

import re
main_word = input('Введите слово -> ')
try:
    index = int(input('Введите число -> '))
except NameError:
     print('К сожалению такого элемента в данном слове нет')

if index <= len(main_word):
    print(f"The {str(index)} symbol in {main_word}, is {str(main_word[index - 1])}")
elif index > len(main_word):
    new_index = input(f'Вы можете выбрать другой индэкс от 1 до {len(main_word)} ->')
    try:
        print(f"The {str(index)} symbol in {main_word}, is {str(main_word[new_index - 1])}")
    except IndexError:
        print('???')#Не могу до конца решить проблему с литералами и всеми возможными по кругу ошибками , можно подсказку плз?)


# 2 Вести з консолі строку зі слів (або скористайтеся константою). Напишіть код, який визначить кількість кількість слів, в цих даних.

string = str(input('Введите предложение: '))
print(len(string.split()))

# 3 Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть механізм, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

all_types_list = input()
str_list = ''.join(str(x) for x in all_types_list)
enumeration_list = [re.sub('\D+', '', i) for i in str_list]
for i in enumeration_list:
    if i == "":
        enumeration_list.remove(i)

print(enumeration_list)#Вроде тоже лучше работает, но много где тупит , я просто не понимаю за что еще зацепится?