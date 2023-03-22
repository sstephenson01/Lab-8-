# Sarah Stephenson and Breanna Eafon
def count_character(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count
print (count_character("bonobos","o"))
