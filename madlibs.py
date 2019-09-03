class wordContainer:

    def __init__(self):
        self.listOfWords = []
        self.wordType = []

    def addWord(self, w, ty):
        self.listOfWords.append(w)
        self.wordType.append(ty)

    def getWord(self):
        word = []
        word.append(self.listOfWords.pop(0))
        word.append(self.wordType.pop(0))
        return word


wC = wordContainer()


def inputWord(wordT, aWT, amount):
    for i in range(amount):
        print("\033[1;32;40m" + str(i) + "/" + str(amount) + "\033[1;37;40m")
        word = input("Please enter a " + wordT + ".\n")
        word = word.split(" ")[0]

        wC.addWord(word, aWT)
        print("Word added.\n")


madlibs = "Yesterday, <p> and I went to the park. On our way to the <a> park, we saw a <a> <n> on a bike. We also saw big <a> balloons tied to a <n>. Once we got to the <a> park, the sky turned <a>. It started to <v> and <v>. <p> and I <v> all the way home. Tomorrow we will try to go to the <a> park again and hope it doesn't <v>."


def swapWord(word):
    looper = len(word.listOfWords)
    text = madlibs

    for i in range(looper):
        sw = word.getWord()
        print(sw)
        text = text.replace(str(sw[1]), str(sw[0]), 1)

    return text


inputWord("person", "<p>", 2)
inputWord("ajective", "<a>", 6)
inputWord("noun", "<n>", 2)
inputWord("verb", "<v>", 4)

print(swapWord(wC))
