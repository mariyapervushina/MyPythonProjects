def is_password_good(password):
    if len(password) < 8:
        return False
    
    upper = False
    lower = False
    digit = False
    
    for char in password:
        if char.isupper():
            upper = True
        if char.islower():
            lower = True
        if char.isdigit():
            digit = True
    
    return upper and lower and digit


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))