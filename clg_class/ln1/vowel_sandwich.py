def is_vowel(char):
    vowel = 'aeiou'
    char.lower()
    return char in vowel
def vowel_sandwich(text):
    vs = False
    for i in range(1,len(text)-1):
        curr = text[i]
        prev = text[i-1]
        nxt = text[i+1]
        if is_vowel(curr) and not is_vowel(prev) and not is_vowel(nxt):
            vs = True
    return vs
result = vowel_sandwich('ab')
if result:
    print(f"true")
else: 
    print('false')