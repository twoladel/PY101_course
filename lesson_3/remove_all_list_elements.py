# Two ways to remove all elements from list
numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4]
del numbers[:]
print(numbers)

# LS solution
numbers = [1, 2, 3, 4]
while numbers:
    numbers.pop()

print(numbers)