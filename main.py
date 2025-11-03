
import sys


def get_book_text(path_to_file):
#takes a filepath and returns the contents of the file as a string
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# def count_words(text):
#     words = text.split()
#     counter = 0
#     for word in words:
#         counter += 1
#         #print(word)
#         #print(counter)
#     return counter

from stats import count_words
from stats import get_characters
from stats import create_charlist
from stats import print_sorted





    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        
    print("============ BOOKBOT ============")
    #print("Analyzing book found at books/frankenstein.txt")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print("Found", count_words(get_book_text(path_to_file)), "total words")
    print("--------- Character Count -------") 
    characters = get_characters(get_book_text(path_to_file))
    #print(characters)
    
    create_charlist(characters)
    print_sorted()
main()
