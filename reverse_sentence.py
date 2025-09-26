def reverseSentence(sentence):
    lst = sentence.split(" ")
    start = 0
    end = len(lst)-1
    while start < end:
        lst[start],lst[end] = lst[end],lst[start]
        start += 1
        end -= 1
    rev_sentence = ""
    for i in lst:
        rev_sentence += i + " "
    return rev_sentence
print(reverseSentence("Hello World this is python programming"))