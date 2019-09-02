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

    def getSize():
        return len(listofWords)


wC = wordContainer()


def inputWord(wordT, aWT, amount):
    for i in range(amount):
        word = inputWord("Please enter a " + wordT)
        word = word.split(" ")[0]

        wordContainer.addWord(word, aWT)


madlibs = "Yesterday, <p> and I went to the park. On our way to the <a> park, we saw a <a> <n> on a bike. We also saw big <a> balloons tied to a <n>. Once we got tot he <a> park, the sky turned <a>. It started to <v> and <v>. <p> and I <v> all the way home. Tomorrow we will try to go to the <a> park again and hope it doesn't <v>."


def swapWord(word):
    looper = word.getSize()

    for i in range(looper):
        sw = word.getWord()
        madlibs.replace(sw[1], sw[0], 1)
