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

        for j in range(self.rows):
            subList = []
            for i in range(self.cols):
                subList.append(0)
            self.Mat.append(subList)
        for k in range(len(self.Mat)):
            for i in range(len(self.Mat[0])):
                print(self.Mat)
                self.Mat[k][i] += int(input(f"Entry for {k+1}{i+1}:- "))

    def initMat(self):
        self.Mat = []
        for j in range(self.rows):
            subList = []
            for i in range(self.cols):
                subList.append(0)
            self.Mat.append(subList)

    def Transpose(self):
        if self.rows == self.cols:
            for i in range(len(self.Mat)):
                for j in range(i + 1, len(self.Mat[0])):
                    temp = self.Mat[i][j]
                    self.Mat[i][j] = self.Mat[j][i]
                    self.Mat[j][i] = temp
            return self.Mat
        return "Tranpose possible on Square Matrices only!, Try diff Matrix"

    def Multi(self, B):
        if self.rows == B.cols:
            C = Matrix(len(self.Mat), len(self.Mat[0]))
            C.initMat()
            for l in range(len(self.Mat)):
                for k in range(len(B.Mat[0])):
                    i = 0
                    j = 0
                    while i < len(self.Mat[0]) and j < len(B.Mat):
                        C.Mat[l][k] += self.Mat[l][i] * B.Mat[j][k]
                        i += 1
                        j += 1
        else:
            return "Multiplication not Possible"


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
        response = A.Add(B)
        if type(response) == list:
            print(f"Multiplication of given matrices are:- {response} ")
        else:
            print(response)
    elif choice == 4:
        while True:
            print("1. Perform A - B")
            print("2. Perform B - A")
            print("3. Back to Menu")
            choiceSub = int(input("Enter Choice:- "))
            if choiceSub == 3:
                break
            elif choiceSub == 1:
                response = A.Sub(B)
                if type(response) == list:
                    print(f"Multiplication of given matrices are:- {response} ")
                else:
                    print(response)
            elif choiceSub == 2:
                iresponse = B.Sub(A)
                if type(response) == list:
                    print(f"Multiplication of given matrices are:- {response} ")
                else:
                    print(response)
    elif choice == 5:
        while True:
            print("1. Perform A*B ")
            print("2. Perform B*A ")
            print("3. Back to Menu")
            choiceSub2 = int(input("Enter valid Choice:- "))
            if choiceSub2 == 3:
                break
            elif choiceSub2 == 1:
                response = A.Multi(B)
                if type(response) == list:
                    print(f"Multiplication of given matrices are:- {response} ")
                else:
                    print(response)
            elif choiceSub2 == 2:
                response = B.Multi(A)
                if type(response) == list:
                    print(f"Multiplication of given matrices are:- {response} ")
                else:
                    print(response)
            else:
                print("Invalid Option Try Again!")
    elif choice == 6:
        while True:
            print("1. Transpose of Matrix A")
            print("2. Transpose of Matrix B")
            print("3. Back to Menu")
            choiceSub1 = int(input("Enter choice"))
            if choiceSub1 == 3:
                break
            elif choiceSub1 == 1:
                response = A.Transpose()
                if type(response) == list:
                    print(f"Transpose of given matrice is:- {response} ")
                else:
                    print(response)
            elif choiceSub1 == 2:
                response = B.Transpose()
                if type(response) == list:
                    print(f"Transpose of given matrice is:- {response} ")
                else:
                    print(response)
            else:
                print("Invalid Option, Try again!")
