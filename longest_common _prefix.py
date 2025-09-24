def longest_common_prefix(words):
    if not words:
        return ''
    words.sort()
    first = words[0]
    last = words[-1]
    i = 0
    while i < len(first) and i < len(last) and last[i] == first[i]:
        i += 1
    return first[:i]
print(longest_common_prefix(["aa","ab",""]))
