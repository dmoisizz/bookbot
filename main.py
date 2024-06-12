def main():
    book_path = "books/frankenstein.txt"
    with open(book_path, "rt") as f:
        file_contens = f.read()

    words = count_words(file_contens)
    characters = count_characters(file_contens)

    print(f'--- Begin report of {book_path} ---')
    print(f"{words} words found in the document\n")

    for char, count in sorted(characters.items(), key=lambda i: i[1], reverse=True):
        print(f"The '{char}' character was found {count} times")

    print(" --- End report ---")


def count_words(text):
    words = text.split()

    return len(words)


def count_characters(text):
    counts = {}
    for c in text.lower():
        if not c.isalpha():
            continue

        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1

    return counts


if __name__ == "__main__":
    main()
