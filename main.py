from stats import path_to_file, get_book_text, charc_and_count, sort_on, dict_organize, get_num_words
file_contents = get_book_text(path_to_file)
num_words = get_num_words(file_contents)
list_of_dict = dict_organize(file_contents)


print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for letter in list_of_dict:
    print(f"{letter['char']}: {letter['num']}")
print("============= END ===============")