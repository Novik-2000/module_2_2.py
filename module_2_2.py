first = int(input('Введите число'))
print(first)
second = int(input('Введите число'))
print(second)
third = int(input('Введите число'))
print(third)
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif third != second != first:
    print(0)
