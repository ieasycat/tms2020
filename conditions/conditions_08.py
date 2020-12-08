"""
Ввести почтовый адрес.
Проверить доменной имя.
В случае если оно gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись “DOMAIN NAME is not supported’
"""

email = input("Введите Ваш электронный адрес: ")
email_check = email.split("@")
if email_check[-1] == "gmail.com":
    print(email)
else:
    print("DOMAIN NAME is not supported")