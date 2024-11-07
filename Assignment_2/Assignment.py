"""
Write a Python program to compute following operations on String: 
a) To display word with the longest length 
b) To determines the frequency of occurrence of particular character in the string 
c) To check whether given string is palindrome or not  
d) To display index of first appearance of the substring  
e) To count the occurrences of each word in a given string 
"""

inputString = input("Enter the string to be manipulated:- ")


def longestLength():
    words = inputString.split()
    maxLength = len(words[0])
    maxLengthWord = words[0]
    for i in range(len(words)):
        if len(words[i]) > maxLength:
            maxength = len(words[i])
            maxLengthWord = words[i]
    return [maxLength, maxLengthWord]


def freqGenerator(subChar):
    words = inputString.split()
    # print(words)
    freq = 0
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j].lower() == subChar.lower():
                freq += 1
    if freq:
        return freq
    return "Not Present"


def palin():
    flag = True
    lengString = len(inputString)
    for i in range(lengString):
        # print(f"{inputString[i]} ?=  {inputString[lengString - i - 1]}")
        if inputString[i] != inputString[lengString - i - 1]:
            flag = False
            break
    return flag


def firstIndex(subWord):
    flag = False
    i = 0
    j = 0
    while i < len(inputString):
        c = i
        while j < len(subWord):
            if i < len(inputString):
                if inputString[i] != subWord[j]:
                    j = 0
                    break
                i += 1
                j += 1
            else:
                break

        if j == len(subWord):
            flag = True
            break
        else:
            i = c
            i += 1
    if flag:
        return i - j + 1
    return "Word not present"


def freqGeneratorWords():
    words = inputString.split()
    freq = {}
    for i in range(len(words)):
        freq[words[i]] = 0
    for i in range(len(words)):
        freq[words[i]] += 1

    return freq


while True:
    print("\nString Manipulation Menu:")
    print(
        "1) To display word with the longest length \n2) To determines the frequency of occurrence of particular character in the string \n3) To check whether given string is palindrome or not \n4) To display index of first appearance of the substring  \n5) To count the occurrences of each word in a given string  \n6) Exit."
    )
    choice = int(input("Enter your choice:- "))
    if choice == 6:
        break
    elif choice == 1:
        print(
            f"The longest word in the given string is {longestLength()[1]} and it's length is {longestLength()[0]}. "
        )
    elif choice == 2:
        subWord = input("Enter the character to find frequency:- ")
        print(
            f"The frequency of occurrence of {subWord} in the given string is:- {freqGenerator(subWord)}"
        )
    elif choice == 3:
        if palin():
            print("Given string is Palindrome.")
        else:
            print("Given string is not Palindrome. ")
    elif choice == 4:
        subStr = input("Enter the SubString:- ")
        if type(firstIndex(subStr)) == int:
            print(
                f"The index of first appearance of the substring {subStr}:- {firstIndex(subStr)} "
            )
        else:
            print({firstIndex(subStr)})
    elif choice == 5:
        print(
            f"The occurrences of each word in a given string are:{freqGeneratorWords()}"
        )
    else:
        print("Invalid Option, Try again")
