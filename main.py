import sys
from stats import character_count, get_sorted_character_count


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    book_text = get_book_text(filepath)
    if book_text is not None:
        # Word Count
        words = book_text.split()
        num_words = len(words)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        # Character Count
        char_counts = character_count(book_text)
        sorted_char_counts = get_sorted_character_count(char_counts)
        print("--------- Character Count -------")

        for item in sorted_char_counts:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===========================")


if __name__ == "__main__":
    main()
