def countChar(char, text):
    count = 0

    for c in text:
        if c == char:
            count += 1

    return count


def countVowels(text):
    vowels = "aeiou"
    count = 0

    for vowel in vowels:
        count += countChar(vowel, text)

    return count


def countWords(text):
    words = text.split()
    return len(words)


# Test
print(countChar("a", "Thailand"))
print(countVowels("Bangkok"))
print(countWords("Human and AI can make mistakes"))