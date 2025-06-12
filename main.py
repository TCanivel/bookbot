import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_book_text, charc_and_count, sort_on, dict_organize, get_num_words
path_to_file = sys.argv[1]
file_contents = get_book_text(path_to_file)
num_words = get_num_words(file_contents)
list_of_dict = dict_organize(file_contents)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_file}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for letter in list_of_dict:
    print(f"{letter['char']}: {letter['num']}")
print("============= END ===============")