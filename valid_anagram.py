def ValidAnagram(str_1, str_2):
    if sorted(str_1) == sorted(str_2):
        return "Valid Anagram"
    return "Invalid Anagram"
print(ValidAnagram("listen","silent"))
print(ValidAnagram("hello","world"))
