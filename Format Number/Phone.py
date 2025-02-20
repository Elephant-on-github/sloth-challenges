import re

def format_phone_number(number):
    number =  f"({number[:3]}) {number[3:6]}-{number[6:]}"
    number = re.sub(r'[^-9()1234567890]', '', number)
    number = number[:5]+" " + number[5:]
    return number

print(format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

print(format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]))

print(format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]))