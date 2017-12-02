import sys

def formal(inText):
    outText = ""
    return outText

def informal(inText):
    outText = ""
    return outText

def main():
    if len(sys.argv) != 3:
        raise ValueError('Invalid input - requires two parameters')
    else:
        mode = sys.argv[1]
        file = open(sys.argv[2], "r")
        inText = file.read()
        if mode == 'formal':
            print(formal(inText))
        elif mode == 'informal':
            print(informal(inText))
        else:
            raise ValueError('Invalid mode type')

if __name__ =='__main__':
    main()
