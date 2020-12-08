# Создать словарь, добавить новую пару, изменить значение нового ключа, вывести все на экран

one = {'a': 30, 'b': 40}
print(one)
one['alex'] = -42
print(one['alex'])
one['alex'] = 55
print(one['alex'])
one.pop('alex')
print(one)