def count_words(text):
    words = text.split()
    return len(words)

def count_unique_characters(text):
    unique_characters = {}
    for char in text:
        if char not in unique_characters:
            unique_characters[char] = 0
        unique_characters[char] += 1
    return unique_characters