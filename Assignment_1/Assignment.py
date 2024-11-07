"""
Problem Statement
In second year computer engineering class, group A student’s play cricket, group B 
students play badminton and group C students play football.  

Write a Python program using functions to compute following: -  
a) List of students who play both cricket and badminton  
b) List of students who play either cricket or badminton but not both  
c) Number of students who play neither cricket nor badminton 
d) Number of students who play cricket and football but not badminton. 

(Note- While realizing the group, duplicate entries should be avoided, Do not use SET 
built-in functions)  """

allStu = []
crickFav = []
footFav = []
badminFav = []

# Entering All students
numOfAllStu = int(input("Enter the Total number of students in the Class:- "))
print("Enter the Students below: ")
for i in range(numOfAllStu):
    allStu.append(int(input(f"Enter the roll n.o of the student {i+1} :- ")))


# Cricket favs
numofCrickFav = int(
    input(
        "Enter the Total number of students in the Class whose favourite sport is Cricket:- "
    )
)
print("Enter the Students below: ")
for i in range(numofCrickFav):
    crickFav.append(int(input(f"Enter the roll n.o of the student {i+1} :- ")))

# Football favs
numofFootFav = int(
    input(
        "Enter the Total number of students in the Class whose favourite sport is Football:- "
    )
)
print("Enter the Students below: ")
for i in range(numofFootFav):
    footFav.append(int(input(f"Enter the roll n.o of the student {i+1} :- ")))


# Badminton favs
numofBadminFav = int(
    input(
        "Enter the Total number of students in the Class whose favourite sport is Badminton:- "
    )
)
print("Enter the Students below: ")
for i in range(numofBadminFav):
    badminFav.append(int(input(f"Enter the roll n.o of the student {i+1} :- ")))


def crickAndBadmin():
    # using Direct functions , ye kar sakte hai!
    # crickAndFoot = set(crickFav) & set(footFav)

    #  nahi toh loops direct
    crickAndBadminList = []
    for i in range(numofBadminFav):
        for j in range(numofCrickFav):
            print(f"i={i},j={j}")
            if badminFav[i] == crickFav[j]:
                crickAndBadminList.append(badminFav[i])
    return crickAndBadminList


def crickOrBadminNotBoth():
    crickOrBadminNotBothList = []
    crickAndBadminList = crickAndBadmin()

    # add all crick
    for i in range(numofBadminFav):
        crickOrBadminNotBothList.append(badminFav[i])

    # add all foot
    for i in range(numofCrickFav):
        crickOrBadminNotBothList.append(crickFav[i])

    # sub all crick and foot
    k = len(crickOrBadminNotBothList) - 1
    while k >= 0:
        for j in range(len(crickAndBadminList)):
            if crickOrBadminNotBothList[k] == crickAndBadminList[j]:
                crickOrBadminNotBothList.pop(k)
                break
        k -= 1

    return crickOrBadminNotBothList


def noCrickNobadmin():
    noCrickNobadminList = []
    for i in range(numOfAllStu):
        noCrickNobadminList.append(allStu[i])

    k = len(noCrickNobadminList) - 1
    while k >= 0:
        for j in range(numofCrickFav):
            if noCrickNobadminList[k] == crickFav[j]:
                noCrickNobadminList.remove(noCrickNobadminList[k])
                break
        for j in range(numofBadminFav):
            if noCrickNobadminList[k] == badminFav[j]:
                noCrickNobadminList.remove(noCrickNobadminList[k])
                break
        k -= 1
    return noCrickNobadminList


def crickAndFootNoBadmin():
    crickAndFootNoBadminList = []
    crickAndBadminList = crickAndBadmin()
    for i in range(len(crickAndBadminList)):
        crickAndFootNoBadminList.append(crickAndBadminList[i])

    k = len(crickAndFootNoBadminList) - 1
    while k >= 0:
        for j in range(numofBadminFav):
            if crickAndFootNoBadminList[k] == badminFav[j]:
                crickAndFootNoBadminList.remove(crickAndFootNoBadminList[k])
                break
        k -= 1
    return crickAndFootNoBadminList


while True:
    print("----------Menu----------")
    print("1.List of students who play both cricket and badminton")
    print("2.List of students who play either cricket or badminton but not both")
    print("3.Number of students who play neither cricket nor badminton ")
    print("4.Number of students who play cricket and football but not badminton.  ")
    print("5.Exit.")
    choice = int(input("Enter ur choice:- "))
    if choice == 5:
        break
    elif choice == 1:
        print(f"Students who play both cricket and badminton:- {crickAndBadmin()}")
    elif choice == 2:
        print(f"Students who play both cricket or badminton:- {crickOrBadminNotBoth()}")
    elif choice == 3:
        print(f"Students who play neither cricket nor badminton:- {noCrickNobadmin()}")
    elif choice == 4:
        print(
            f"Students who play cricket and football but not badminton:- {crickAndFootNoBadmin()}"
        )
    else:
        print("Invalid Choice, Try again!")
