from stats import path_to_file, get_book_text, charc_and_count
file_contents = get_book_text(path_to_file)
dictionary_of_chars_and_counts = charc_and_count(file_contents)
print(dictionary_of_chars_and_counts)
