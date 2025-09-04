def count_words(text):
    words = text.split()
    return len(words)

def count_unique_characters(text):
    unique_characters = {}
    for char in text:
        if char.isalpha() is False:
            continue
        lower_char = char.lower()
        if lower_char not in unique_characters:
            unique_characters[lower_char] = 0
        unique_characters[lower_char] += 1
    return sort_character_dictionary(unique_characters)

def sort_character_dictionary(char_dict):
    list_of_dicts = []
    for key, value in char_dict.items():
        list_of_dicts.append({"char": key, "num": value})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(item):
    return item["num"]