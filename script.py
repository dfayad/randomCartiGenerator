import lyricwikia
import random

lyrics = lyricwikia.get_lyrics('Playboi Carti', 'Magnolia')
#print(lyrics)


words = lyrics.split(' ')
#print('-----')
#print(words)

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


#print('-----------')
#print(cleanWords)

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

def getRandomWord(dictionary):
    rand = random.randint(0,len(dictionary)-1)
    word = dictionary[rand]
    return word

def makeChorus(dictionary, wordPerLine):
    lines = []
    for i in range(2):
        line = makeLine(dictionary, wordPerLine)
        lines.append(line)
    lines = lines + lines
    paragraph = '\n'.join(lines)
    return paragraph

def getSong():

    title = getRandomWord(cleanWords) + ' ' + getRandomWord(cleanWords)
    chorus = makeChorus(cleanWords, 5)
    v1 = makeVerse(cleanWords, 5, 12)
    v2 = makeVerse(cleanWords, 6, 10)
    v3 = makeVerse(cleanWords, 4, 8)

    print('------------------------')
    print('Name of the song: '+title)
    print('Verse 1--------')
    print(v1)
    print('Chorus--------')
    print(chorus)
    print('Verse 2--------')
    print(v2)
    print('Chorus--------')
    print(chorus)
    print('Verse 3--------')
    print(v3)

