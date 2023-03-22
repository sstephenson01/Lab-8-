# Sarah Stephenson and Breanna Eafon
def count_letter(s):
    count = 0
    for char in s:
        count += len(char)
    return count

print (count_letter(["dog", "cat"]))
