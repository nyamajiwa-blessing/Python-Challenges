# Find the longest word in a sentence
def longest_word(sentence):
    longest_word = ''
    words = sentence.split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def main():
    sentence = input("Enter a sentence: ")
    longest = longest_word(sentence)
    print(f"The longest word is: {longest}")

main()