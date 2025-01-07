print("hello world")

def main():
    print(get_book_content("books/frankenstein.txt"))
    print(count_words("books/frankenstein.txt"))
    print(count_chars("books/frankenstein.txt"))
    print_chars_stats("books/frankenstein.txt")

def get_book_content(bookfile):
    with open(bookfile) as f:
        file_contents = f.read()
    return file_contents

def count_words(bookfile):
    content = get_book_content(bookfile)
    words = len(content.split())
    return words

def count_chars(bookfile):
    content = get_book_content(bookfile).lower()
    char_count = {}
    for char in content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_chars_stats(bookfile):
    chars = count_chars(bookfile)
    sum_chars = sum(chars.values())
    print(f"{sum_chars} words found in the document")
    for key, value in chars.items():
        print(f"The '{key}' character was found {value} times")



main()
