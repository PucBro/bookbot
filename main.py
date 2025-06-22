from stats import get_word_count,  get_chars, sorted_dicts

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count('books/frankenstein.txt')} total words") 
    print("--------- Character Count -------")
    for item in sorted_dicts('books/frankenstein.txt'):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
