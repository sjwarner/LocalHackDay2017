import sys

def translate(inText, dictionary_path):

    inText.split()

    formal_dictionary = {}
    dictionaryFile = open(dictionary_path, 'r')
    dictionaryText = dictionaryFile.read()
    dictionaryFile = open(dictionary_path, 'r')

    # Populate the dictionary with the contents of text file
    for i in range(dictionaryText.count("\n")):
        line = dictionaryFile.readline()
        formal_dictionary[line.strip().split(',')[0]] = line.strip().split(',')[1]

    inTextList = inText.split(" ")
    outText = ""

    for i in range(len(inTextList)):
        if inTextList[i] in formal_dictionary:
            outText += (" " + formal_dictionary.get(inTextList[i]))
        else:
            outText = outText + " " + inTextList[i]

    return outText

def main():
    if len(sys.argv) != 3:
        raise ValueError('Invalid input - requires two parameters')
    else:
        mode = sys.argv[1]
        file = open(sys.argv[2], "r")
        
        inText = file.read()
        
        outFile = open("translatedEmail.txt", "w")

        if mode == 'formal':
            outFile.write(translate(inText, "formalDictionary.txt"))
        elif mode == 'informal':
            outFile.write(translate(inText, "informalDictionary.txt"))
        else:
            raise ValueError('Invalid mode type')

if __name__ =='__main__':
    main()
