def get_num_words(book):
    """
    accepts the text from the book as a string,
    and returns the number of words in the string
    """
    return len(book.split())

def character_use(book):
    """
    takes the text from the book as a string,
    and returns the number of times each character,
    (including symbols and spaces), appears in the string
    """
    lower_case = book.lower()

    char_counts = {}
    for char in lower_case:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sorted_char_counts(char_dict):
    """
    takes the dictionary of characters and their counts and
    returns a sorted list of dictionaries
    """
    char_list = []
    for (char, num) in char_dict.items():
        pair_dict = {}
        pair_dict["char"] = char
        pair_dict["num"] = num
        char_list.append(pair_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(items):
    return items["num"]