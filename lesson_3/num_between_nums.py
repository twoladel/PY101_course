def num_between_10_100(num):
    return num in range(10, 101)

print(num_between_10_100(42))
print(num_between_10_100(100))
print(num_between_10_100(101))

print(42 in range(1, 101))
print(100 in range(1, 101))
print(101 in range(1, 101))