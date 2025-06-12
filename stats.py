def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()  
    return file_contents

    book_text = get_book_text(path_to_file)

def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def charc_and_count(book_text):
    charc_count_dict = {}
    words = book_text.split()
    for word in words:
        lower_case_word = word.lower()
        for letter in lower_case_word:
            if letter.isalpha() != True:
                continue
            if letter not in charc_count_dict:
                charc_count_dict[letter] = 1
            else:
                charc_count_dict[letter] += 1
    return charc_count_dict

def sort_on(dict):
    return dict["num"]

def dict_organize(file_contents):
    list_of_dict = []
    dict_to_organize = charc_and_count(file_contents)
    for letter, count in dict_to_organize.items():
        diction = {"char" : letter, "num" : count}
        list_of_dict.append(diction)
    list_of_dict.sort(reverse = True, key = sort_on)
    return list_of_dict

def main():
    file_contents = get_book_text(path_to_file)
    get_num_words(file_contents)
    charc_and_count(file_contents)
    dict_organize(file_contents)