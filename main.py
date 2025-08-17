from stats import get_word_count
from stats import get_char_count
from stats import sort_dict

def get_book_text(book_dir: str) -> str:
    with open(book_dir) as f:
        return f.read()

def print_stats(text):
    wc = get_word_count(text)
    cc = get_char_count(text)
    sort_cc = sort_dict(cc)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for char_count in sort_cc:
        print(f"{char_count['char']}: {char_count['num']}")


def main():
    book_dir = "./books/frankenstein.txt"
    text = get_book_text(book_dir)
    print_stats(text)


if __name__ == "__main__":
    main()

