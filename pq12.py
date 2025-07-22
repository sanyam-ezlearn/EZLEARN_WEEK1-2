'''Finding Uncommon Words from Two Sentences'''
def uncommonFromSentences(s1, s2):
    words1 = s1.split()
    words2 = s2.split()

    counts = {}
    for word in words1 + words2:
        counts[word] = counts.get(word, 0) + 1

    uncommon = [word for word in counts if counts[word] == 1]
    return uncommon

s1 = "this apple is sweet"
s2 = "this apple is sour"
print(uncommonFromSentences(s1, s2))