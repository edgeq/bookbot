import sys
from stats import get_num_words, character_use, sorted_char_counts

def get_book_text(filepath):
    # with block frees up resources after completion
    with open(filepath) as f:
        # return read stream - we can print it later
        return f.read()

def main():
    print(f"{sys.argv}")
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        # assign read stream to text
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        char_counts = character_use(text)
        sorted_chars = sorted_char_counts(char_counts)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in sorted_chars:
            if char["char"].isalpha():
                print(f"{char["char"]}: {char["num"]}")

main()