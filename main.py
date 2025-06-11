path_to_file = "books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def words_in_text(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def main():
    file_contents = get_book_text(path_to_file)
    words_in_text(file_contents)

main()
