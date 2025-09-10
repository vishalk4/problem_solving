def consonant_vowels(string):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonant_count = 0
    for i in string:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            if i in vowels:
                vowels_count += 1
            else:
                consonant_count += 1
    return f"no.of vowels : {vowels_count}", f"no.of consonants : {consonant_count}"
print(consonant_vowels("                         "))