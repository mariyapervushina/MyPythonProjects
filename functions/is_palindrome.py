# объявление функции
def is_palindrome(text):
    text = "".join(i for i in text if i.isalpha())
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))