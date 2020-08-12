from collections import Counter

with open('DATA/words.txt') as words_in:
    letters = [word[0] for word in words_in]

print(letters[:100], len(letters))

counts = Counter(letters)
print(counts)

print(counts.most_common(5))

