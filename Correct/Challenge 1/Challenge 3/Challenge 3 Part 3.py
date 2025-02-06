word = input("Input a word: ")
wordlst = list(word.lower())
vowels = ["a", "e", "i", "o", "u"]
x = 0

def numvow(x):
    for i in word:
        if i in vowels:
            x  = x + 1
    return x

print(numvow(x))