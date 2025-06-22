from stats import get_word_count

def main():
    print(f"{get_word_count(get_book_text('books/frankenstein.txt'))} words found in the document") 

main()
