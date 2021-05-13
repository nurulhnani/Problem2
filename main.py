import urllib.request, urllib.error, urllib.parse
import web
import trie

url = 'https://www.dailymail.co.uk/news/article-2889112/A-million-parcels-stuck-depots-failure-courier-City-Link.html'

response = urllib.request.urlopen(url)
html = response.read()
text = web.stripTags(html).lower()
fullwordlist = web.stripNonAlphaNum(text)
wordlist1 = web.remove(fullwordlist)
wordlist2 = web.removeStopwords(wordlist1, web.stopwords)
dictionary = web.wordListToFreqDict(wordlist2)
sorteddict = web.sortFreqDict(dictionary)

#for s in sorteddict:
#    print(str(s))

#print(dictionary.items())
#print(wordlist2)

tr = trie.Trie()

for key, value in dictionary.items():
    tr.insert(key, value)

key1 = []
#badWord
with open("badWord.txt", "r") as a_file:
    total = []
    for line in a_file:
        stripped_line = line.strip()
        output = tr.search(stripped_line)
        if output:
            x = tr.search(stripped_line)[0]
            y = tr.search(stripped_line)[1]
            print(x)
            key1 += x
            total.append(y)

    sumBad = 0
    for i in total:
        sumBad += i
    print('\nTotal Bad Words: ', sumBad)

print('\n-------------------------------------------------------\n')
#postiveWord
with open("positiveWord.txt", "r") as a_file:
    total = []
    for line in a_file:
        stripped_line = line.strip()
        output = tr.search(stripped_line)
        if output:
            x = tr.search(stripped_line)[0]
            y = tr.search(stripped_line)[1]
            print(x)
            key1 += x
            total.append(y)

    sumPos = 0
    for i in total:
        sumPos += i
    print('\nTotal Positive Words: ', sumPos)

print('\n-------------------------------------------------------\n')

for j in key1:
    key = str(j)
    dictionary.pop(key)
#print(main.dictionary.items())

sumNeu = 0
for key, value in dictionary.items():
    sumNeu += value
neutralWord = list(dictionary.keys())
print(neutralWord)
#print(main.dictionary.keys())
print('\nTotal Neutral Words: ', sumNeu)
