def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())
