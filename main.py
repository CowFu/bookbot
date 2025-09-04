import sys

from stats import count_words, count_unique_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for char in count_unique_characters(book_text):
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        file_contents = f.read()
        return file_contents


main()