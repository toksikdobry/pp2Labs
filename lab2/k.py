sent = input()
sent = sent.replace('.', '').replace(',', '').replace('?', '').replace('!', '').split()
uniqueWords = []
for word in sent: 
    if word not in uniqueWords: uniqueWords.append(word)
uniqueWords.sort()
print(len(uniqueWords))
print(*uniqueWords, sep = '\n')