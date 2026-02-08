alphabet = input("Enter a letter: ").lower()

if not alphabet.isalpha() or len(alphabet) != 1:
    print("Invalid input")
elif alphabet in {'a', 'e', 'i', 'o', 'u'}:
    print("Vowel")
else:
    print("Consonant")
