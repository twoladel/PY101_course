str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

def find_sub(string):
    return 'Dino' in string

print(find_sub(str1))
print(find_sub(str2))