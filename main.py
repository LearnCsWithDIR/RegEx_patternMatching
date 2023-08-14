def lpsArray(pattern):
    length = 0
    lps = [0] * len(pattern)
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(pattern, text):
    i = 0
    j = 0
    lineNumber = 1
    charCount = 0
    lps = lpsArray(pattern)
    positionList = []
    while i < len(text):
        if text[i] == '\n':
            lineNumber += 1
            charCount = i + 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len(pattern):
                positionList.append([lineNumber, i - (j + charCount)])
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positionList


def dot_search(pattern, text):
    i = 0
    j = 0
    lineNumber = 1
    charCount = 0
    lps = lpsArray(pattern)
    positionList = []
    while i < len(text):
        if text[i] == '\n':
            lineNumber += 1
            charCount = i + 1
        if pattern[j] == text[i] or pattern[j] == '.':
            i += 1
            j += 1
            if j == len(pattern):
                positionList.append([lineNumber, i - (j + charCount)])
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positionList


def question_search(pattern,text):
    ptr1 = ""
    ptr2 = ""
    for i in pattern:
        if i != '?':
            ptr1 += i
            ptr2 += i
        else:
            ptr2 = ptr2[:-1]

    positionList = kmp_search(ptr1, text)
    for i in kmp_search(ptr2, text):
        if i not in positionList:
            positionList.append(i)

    sortedPositionList = sorted(positionList, key=lambda x: (x[0], x[1]))

    return sortedPositionList


def startWith_search(pattern, text):
    pattern = pattern[1:]
    i = 0
    j = 0
    lineNumber = 1
    charCount = 0
    lps = lpsArray(pattern)
    positionList = []
    condition = True
    while i < len(text):
        if text[i] == '\n':
            lineNumber += 1
            charCount = i + 1
        if i - charCount == 0 or text[i - 1] == ' ':
            condition = True
        if condition:
            if pattern[j] == text[i]:
                i += 1
                j += 1
                if j == len(pattern):
                    positionList.append([lineNumber, i - (j + charCount)])
                    j = lps[j - 1]
                    condition = False
            else:
                condition = False
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        else:
            i += 1

    return positionList


def endWith_search(pattern, text):
    pattern = pattern[1:]
    text += '\0'
    i = 0
    j = 0
    k = 0
    lineNumber = 1
    charCount = 0
    lps = lpsArray(pattern)
    positionList = []
    sign = [' ', '\n', '\0']
    while i < len(text):
        if text[i] == '\n':
            lineNumber += 1
            charCount = i + 1
        if text[i] in sign:
            k = i + 1 - (j + charCount)
        if j != len(pattern):
            if pattern[j] == text[i]:
                i += 1
                j += 1
                if j == len(pattern) and not text[i].isalpha():
                    positionList.append([lineNumber, k])
                    j = lps[j - 1]
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positionList


flag = True
n = 0
while flag:
    if n == 0:
        # get the user inputs
        pattern = input("Enter the pattern : ")
        outputFile = open('Output.txt', "w")

    elif n > 0:
        try:
            flag = int(input("Do you want to search again another pattern (0 or 1) :"))
            # continue for get the user inputs
            if flag:
                pattern = input("Enter the pattern : ")

        except ValueError:
            print("******* Error: Invalid input. Please enter a valid number ********")

    if flag:
        # read the input file include text
        textFile = open('input.txt', "r")

        text = textFile.read().strip()

        if '^' in pattern:
            positionList = startWith_search(pattern, text)
        elif '.' in pattern:
            positionList = dot_search(pattern, text)
        elif '?' in pattern:
            positionList = question_search(pattern, text)
        elif '$' in pattern:
            positionList = endWith_search(pattern, text)
        else:
            # normal string pattern searching
            positionList = kmp_search(pattern, text)

        if positionList:
            outputFile.write(str(n + 1) + " Search pattern is " + pattern+"\n")
            outputFile.write("------ Total " + str(len(positionList)) + " pattern match cases Found! ------\n")
            for line, idx in positionList:
                outputFile.write("Line " + str(line) + ", Index " + str(idx) + "\n")
            outputFile.write("\n")
        else:
            outputFile.write(str(n + 1) + " Search pattern is " + pattern+"\n")
            outputFile.write("This pattern is not Found!\n\n")

        textFile.close()

        print(str(n+1) + " Pattern Matching Processing End!\n")
    else:
        print("Pattern Matching Algorithm is exists.")
        print("Search all patterns are saved in output text file")
    n += 1

outputFile.close()
