def wordCount(text):
    return(len(text.split()))

def sort_on(dict):
    return dict["x"]


def charCount(text):
    words = {}
    for word in text:
        if word.isalpha():
            word = word.lower()
            if word in words:
                words[word]+=1
            else:
                words[word]=1
    print(words)

    return words


def main():
    with open("github.com/Vozikk/bookbot/books/frankenstein.txt") as f:
        text = f.read()
        slova = wordCount(text)
        print(f"{slova} words found in the document")
        print()
        characters = charCount(text)
        for c in characters:
            print(f"The {c} character was found {characters[c]} times")
main()