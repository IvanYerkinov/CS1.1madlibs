class wordContainer:
    listOfWords = []
    wordType = []

    def addWord(w, ty):
        self.listOfWords.append(w)
        self.wordType.append(ty)

    def getWord():
        word = []
        word.append(self.listOfWords.pop(0))
        word.append(self.wordType.pop(0))
        return word


wC = wordContainer()


def inputWord(wordT, aWT, amount):
    for i in range(amount):
        word = inputWord("Please enter a " + wordT)
        word = word.split(" ")[0]

        wordContainer.addWord(word, aWT)
