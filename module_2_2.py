first = 321
print(first)
second = 654
print(second)
third = 987
print(third)
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif third != second != first:
    print(0)

