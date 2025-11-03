def count_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
        #print(word)
        #print(counter)
    return counter


def get_characters(text):
    characters = {}
    tmp = text.lower()
    for char in tmp:
        #print(char)
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return(characters)

def get_num(characters):
    return characters["num"]

charlist = []

def create_charlist(characters):
    
    for char in characters:
        if char.isalpha():
            charlist.append({"char": char, "num": characters[char]})



def print_sorted():
    charlist.sort(reverse=True, key=get_num)
    total_characters = len(charlist)
    #print(charlist)
    for i in range(total_characters):
        tmp_char = charlist[i]["char"]
        tmp_num = charlist[i]["num"]
        print(f"{tmp_char}: {tmp_num}")


