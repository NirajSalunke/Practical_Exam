"""
Write a python program to compute following computation on matrix: 
a) Addition of two matrices 
b) Subtraction of two matrices 
c) Multiplication of two matrices 
d) Transpose of a matrix 
"""


class Matrix:
    def __init__(self, rows, cols):
        self.Mat = []
        self.rows = rows
        self.cols = cols

    def Add(self, B):
        if B.rows == self.rows and B.cols == self.cols:
            C = Matrix(len(self.Mat), len(self.Mat[0]))
            C.initMat()
            for i in range(len(self.Mat)):
                for j in range(len(self.Mat[0])):
                    C.Mat[i][j] = self.Mat[i][j] + B.Mat[i][j]
            return C.Mat
        else:
            return "Matrix Addition is not possible!"

    def Sub(self, B):
        if B.rows == self.rows and B.cols == self.cols:
            C = Matrix(len(self.Mat), len(self.Mat[0]))
            C.initMat()
            for i in range(len(self.Mat)):
                for j in range(len(self.Mat[0])):
                    C.Mat[i][j] = self.Mat[i][j] - B.Mat[i][j]
            return C.Mat
        else:
            return "Matrix Addition is not possible!"

    def enterMat(self):
        self.Mat = []
        self.rows = int(input("Enter number of rows:- "))
        self.cols = int(input("Enter number of cols:- "))
        subList = []
        for i in range(self.cols):
            subList.append(0)
        for j in range(self.rows):
            self.Mat.append(subList)
        for k in range(len(self.Mat)):
            for i in range(len(self.Mat[0])):
                self.Mat[k][i] = int(input(f"Entry for {k+1}{i+1}:- "))

    def initMat(self):
        self.Mat = []
        subList = []
        for i in range(self.cols):
            subList.append(0)
        for j in range(self.rows):
            self.Mat.append(subList)

    def Transpose(self):

        return self.Mat


A = Matrix(0, 0)
B = Matrix(0, 0)
while True:
    print("\n--------Menu-------\n")
    print("--Input--")
    print("1. Enter  Matrix A")
    print("2. Enter  Matrix B")
    print("Note: If not enterd as  entries will zero\n")
    print("--Operations--")
    print("3. Addition")
    print("4. Subraction")
    print("5. Multiplication")
    print("6. Tranpose\n")
    print("7. Exit\n")
    choice = int(input("Enter Valid Choice:- "))

    if choice == 7:
        break
    elif choice == 1:
        A.enterMat()
    elif choice == 2:
        B.enterMat()
    elif choice == 3:
        if type(A.Add(B)) == list:
            print(f" Addition of Given Matrices are:  {A.Add(B)}")
        else:
            print(A.Add(B))
    elif choice == 4:
        print("1. Perform A - B")
        print("2. Perform B - A")
        choiceSub = int(input("Enter Choice:- "))
        if choiceSub == 1:
            if type(A.Sub(B)) == list:
                print(f" Subtraction of Given Matrices are: A - B ={A.Sub(B)}")
            else:
                print(A.Sub(B))
        elif choiceSub == 2:
            if type(B.Sub(A)) == list:
                print(f" Subtraction of Given Matrices are: B - A ={B.Sub(A)}")
            else:
                print(B.Sub(A))

    elif choice == 5:
        print("5")
    elif choice == 6:
        print("1. Transpose of Matrix A")
        print("1. Transpose of Matrix B")
        choiceSub1 = int(input("Enter choice"))
        if choiceSub1 == 1:
            print(f"Transpose of the Matrix is:- {A.Transpose()} ")
        elif choiceSub1 == 2:
            print(f"Transpose of the Matrix is:- {B.Transpose()} ")
        else:
            print("Invalid Option, Try again!")
