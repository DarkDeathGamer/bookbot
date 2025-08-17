from stats import get_word_count

def get_book_text(book_dir: str) -> str:
    with open(book_dir) as f:
        return f.read()

def main():
    book_dir = "./books/frankenstein.txt"
    text = get_book_text(book_dir)
    wc = get_word_count(text)
    print(f"{wc} words found in the document")

if __name__ == "__main__":
    main()

