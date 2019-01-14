import lyricwikia
import random

lyrics = lyricwikia.get_lyrics('Playboi Carti', 'Magnolia')
print(lyrics)


words = lyrics.split(' ')
print('-----')
print(words)

cleanWords = []
#remove all newline symbols
for word in words:
    if '\n' in word:
        word  = word.replace('\n',' ')
        wrds = word.split(' ')
        for w in wrds:
            if w!='':
                cleanWords.append(w)
    else:
        cleanWords.append(word)


print('-----------')
print(cleanWords)

def makeVerse(dictionary, numOfLines, wordPerLine):
    lines = []
    for i in range(numOfLines):
        line = makeLine(dictionary, wordPerLine)
        lines.append(line)
    paragraph = '\n'.join(lines)
    return paragraph

def makeLine(dictionary, wordsPerLine):
    line = []
    for i in range(wordsPerLine):
        rand = random.randint(0,len(dictionary)-1)
        line.append(dictionary[rand])
    lineStr = ' '.join(line)
    return lineStr

v1 = makeVerse(cleanWords, 5, 12)
print('HERES A VERSE')
print(v1)

