def get_book_text(book_dir: str) -> str:
    with open(book_dir) as f:
        return f.read()

def main():
    book_dir = "./books/frankenstein.txt"
    text = get_book_text(book_dir)
    print(text)

if __name__ == "__main__":
    main()

