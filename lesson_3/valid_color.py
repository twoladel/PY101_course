# first solution
def is_color_valid(color):
    return color == "blue" or color == "green"

print(is_color_valid('blue'))
print(is_color_valid('green'))
print(is_color_valid('red'))
print()

# second solution
def is_color_valid(color):
    return not (color == "blue" or color == "green")

print(is_color_valid('blue')) # False
print(is_color_valid('green')) # False
print(is_color_valid('red')) # True
print()

# LS second solution
def is_color_valid(color):
    return color in ['blue', 'green']

print(is_color_valid('blue')) 
print(is_color_valid('green')) 
print(is_color_valid('red'))

