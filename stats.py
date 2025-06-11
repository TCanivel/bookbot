path_to_file = "books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def charc_and_count(file_contents):
    charc_count_dict = {}
    words = file_contents.split()
    for word in words:
        lower_case_word = word.lower()
        for letter in lower_case_word:
            if letter not in charc_count_dict:
                charc_count_dict[letter] = 1
            else:
                charc_count_dict[letter] += 1
    return charc_count_dict
            


def main():
    file_contents = get_book_text(path_to_file)
    get_num_words(file_contents)
    charc_and_count(file_contents)

main()