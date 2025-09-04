from stats import count_words, count_unique_characters

def main():
    book_file_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_file_path)
    print(f"{count_words(book_text)} words found in the document")
    print(count_unique_characters(book_text))

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        file_contents = f.read()
        return file_contents


main()