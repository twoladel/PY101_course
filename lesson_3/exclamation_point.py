def ends_with_exclamation(sentence):
    return sentence.endswith('!')

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(ends_with_exclamation(str1))
print(ends_with_exclamation(str2))

def ends_w_excl(sentence):
    if sentence[-1] == '!':
        return True
    else:
        return False
    
print(ends_w_excl(str1))
print(ends_w_excl(str2))