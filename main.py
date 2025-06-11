path_to_file = "books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def words_in_text(file_contents):
    words = file_contents.split()

    for word in words:
        total_words = word + 1

    return total_words

def main():
    print(words_in_text(file_contents))

main()
