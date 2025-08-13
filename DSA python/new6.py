s = input("Enter a string: ")

char_dict = {}

for index, char in enumerate(s):
    if char in char_dict:
        char_dict[char].append(index)
    else:
        char_dict[char] = [index]

print(char_dict)
