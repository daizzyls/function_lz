text = input("Введите строку: ")


clean_text = "".join(text.split()).lower()

if clean_text == clean_text[::-1]:
    print("Строка является палиндромом!")
else:
    print("Строка не является палиндромом.")
