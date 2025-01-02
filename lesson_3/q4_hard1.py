def is_an_ip_number(num_string):
    if num_string.isdigit():
        return int(num_string) in range(256)
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
        
    return True

print(is_dot_separated_ip_address('244.2.34.56'))
print(is_dot_separated_ip_address('23.135.223.34.45'))
print(is_dot_separated_ip_address('23.355.3.34'))
print(is_dot_separated_ip_address('abc.234.34.55'))
print(is_dot_separated_ip_address('-23.234.34.55'))