def get_num_words(book_text):
    split_words = book_text.split()
    num_words = len(split_words)

    print(f"{num_words} words found in the document")


def character_count(book_text):
    book_text = book_text.lower()

    char_count = {}

    for char in book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def get_sorted_character_count(char_count_dict):
    # convert the character count dictionary to a list of dictionaries
    char_list = [
        {"char": char, "num": count} for char, count in char_count_dict.items()
    ]
    # sort the lsit of dictionaries by the 'num ' key in descendign order
    char_list.sort(key=lambda item: item["num"], reverse=True)

    return char_list
