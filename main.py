from stats import word_count
from stats import char_count
from stats import sort_dict

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_test(path_to_file: str) -> str:
    with open(path_to_file, "r") as file:
        content = file.read()
    return content

def main():    
    path_to_book = sys.argv[1]
    
    content = get_book_test(path_to_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    
    num_words = word_count(content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    chars_dict = char_count(content)
    chars_list = sort_dict(chars_dict)
    print("--------- Character Count -------")
    for char_dict in chars_list:
        char = char_dict["char"]
        chr_count = char_dict["num"]
        
        if not char.isalpha():
            continue
        
        print(f"{char}: {chr_count}")

    print("============= END ===============")
    
main()