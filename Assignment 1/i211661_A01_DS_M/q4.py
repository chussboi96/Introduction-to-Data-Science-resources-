## Question Number 4:
def dictionary():
    d = int(input("Please enter number of words you want in dictionary between 1 - 100: "))
    if d>=1 and d<=100:
        dictionaryLength = d
    else:
        print("Enter the lenght of dictionary between 1 to 100: ")
        d = int(input("Please enter number of words you want in dictionary between 1 - 100: "))
        dictionaryLength = d

    dictionary = {}
    dictwords = []

    for i in range(dictionaryLength):
        word = (input("Enter word: ")).lower()
        if len(word)>=1 and len(word)<=15:
            dictwords.append(word)
        else:
            print("Enter word with more than one character and less than 15 characters: ")
            word = (input("Enter word: ")).lower()
            dictwords.append(word)

    for i in range(dictionaryLength):
        dictionary[i] = dictwords[i]
    print("Your dictionary is: \n", dictionary)

    return dictionary


#make words list
def words():
    wordsList = []
    n = int(input("Enter number of words you want to check: "))
    if n>=1:
        wordsLength = n
    else:
        print("Atleast one word is required to be checked")
        n = int(input("Enter number of words you want to check: "))
        wordsLength = n

    for i in range(wordsLength):
        words = (input("Enter word: ")).lower()
        if len(words)>=1 and len(words)<=15:
            wordsList.append(words)
        else:
            print("Enter word with more than one character and less than 15 characters: ")
            words = (input("Enter word: ")).lower()
            wordsList.append(words)

    print("Your Words List is: \n", wordsList)

    return wordsList


def checkWord(dict_word, userWord):
    x1 = len(dict_word)
    x2 = len(userWord)
    difference = abs(x1 - x2)

    # if difference is greater than 1, words arent similar
    if difference > 1:
        return "Unknown Word"
    elif difference == 0:  # find indices at which characters are difference
        diff_index = []
        for i in range(x1):
            if dict_word[i] != userWord[i]:
                diff_index.append(i)

        difference = len(diff_index)  # counting no. of different letters

        if difference == 0:   # if no. of different letters is 0 & words are similar
            return "Correct Word"
        elif difference == 1:  # if no. of different letters is 2 & words are similar
            return "One letter difference."
        elif difference == 2:  # if no. of different letters is 2 (transposition)
            i = diff_index[0]
            j = diff_index[1]

            if j != i + 1:
                return "Unknown again"
            elif dict_word[i] == userWord[j] and dict_word[j] == userWord[i]:
                return "2 letters transposed in"
            else:
                return "Unknown yet again"
    else:
        bigger = None
        smaller = None
        if x1 > x2:
            bigger = dict_word
            smaller = userWord
        else:
            bigger = userWord
            smaller = dict_word
            indx = 0
            while indx < min(x1, x2) and smaller[indx]==bigger[indx]:
                indx = indx + 1
                if bigger[indx + 1:] == smaller[indx:]:
                    if x1 > x2:
                        return "One letter omitted from"
                    else:
                        return "One letter added"



def main():
    dic = dictionary()
    w = words()
    dictionarylength = len(dic)
    wordLength = len(w)
    for i in range(wordLength):
        for j in range(dictionarylength):
            print(w[i],checkWord(dic[j],w[i]))
            break

main()