"""
Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково
слева направо и справа налево.
(Определить функцию, позволяющую распознавать слова палиндромы.)[03-10.32]
"""


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def main():
    words = 'лол', 'привет', 'река'
    for word in words:
        if palindrome(word):
            print(f'{word} - является палиндромом')
        else:
            print(f'{word} - не является палиндромом')


if __name__ == '__main__':
    main()
