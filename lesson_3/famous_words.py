famous_words = "seven years ago..."

# Solution 1
print("Four score and" + ' ' + famous_words)

#Solution 2
famous_words = "seven years ago..."

print(' '.join(['Four score and', famous_words]))

# LS solution = interpolation
new_famous_words = f"Four score and {famous_words}"
print(new_famous_words)