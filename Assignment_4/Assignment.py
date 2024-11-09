"""
a) Write a pythonprogram to store roll numbers of student in array who attended 
training program in random order. Write function for searching whether particular 
student attended training program or not, using Linear search , Sentinel search, Binary search and Fibonacci search. 
"""


class SearchBy:
    def __init__(self, arr):
        self.studentArray = arr

    def Linear(self, studentRoll):
        for i in range(len(self.studentArray)):
            if self.studentArray[i] == studentRoll:
                return f"Student was Present in Training Program at {i+1}."
        return "Student was absent in Training Program"

    def Sentinel(self, studentRoll):
        self.studentArray.append(studentRoll)
        i = 0
        while self.studentArray[i] != studentRoll:
            i += 1
        self.studentArray.pop()
        if i < len(self.studentArray):
            return f"Student was Present in Training Program at {i+1}."
        else:
            return "Student was absent in Training Program"

    def Binary(self, studentRoll):
        print("Binary")

    def Fibonacci(self, studentRoll):
        print("Fibonacci")


SearchByMethod = SearchBy([])
totalStudents = int(input("Enter Number of Students to add Attendance:- "))
for i in range(totalStudents):
    SearchByMethod.studentArray.append(int(input(f"Enter roll no of student {i+1}:- ")))

while True:
    print("----Menu----")
    print("1. Search by Linear Method")
    print("2. Search by Sentinel Method")
    print("3. Search by Binary Method")
    print("4. Search by Fibonacci Method")
    print("5. Exit")
    choice = int(input("Enter Valid Option:- "))
    if choice == 5:
        break
    elif choice == 1:
        rollNo = int(input("Enter the roll n.o to be Searched:- "))
        print(SearchByMethod.Linear(rollNo))

    elif choice == 2:
        rollNo = int(input("Enter the roll n.o to be Searched:- "))
        print(SearchByMethod.Sentinel(rollNo))

    elif choice == 3:
        print("Binary")
    elif choice == 4:
        print("Fibonacci")
    else:
        print("Invalid Option,Try Again!")
