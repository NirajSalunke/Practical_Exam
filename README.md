# OOP Practical Assignments

This branch contains the Object-Oriented Programming (OOP) assignments. Each assignment is organized in its own folder to facilitate individual testing and debugging in Eclipse.

## Table of Contents

1. [Assignment 1: Complex Number Class](#assignment-1-complex-number-class)
2. [Assignment 2: Student Information System Database](#assignment-2-student-information-system-database)
3. [Assignment 3: Book Shop Inventory System](#assignment-3-book-shop-inventory-system)
4. [Assignment 4: File Input/Output](#assignment-4-file-inputoutput)
5. [Assignment 5: Selection Sort Template](#assignment-5-selection-sort-template)
6. [Assignment 6: STL Sorting and Searching](#assignment-6-stl-sorting-and-searching)
7. [Assignment 7: Map Associative Container for State Populations](#assignment-7-map-associative-container-for-state-populations)

---

### Assignment 1: Complex Number Class

- **Problem Statement**: Implement a class `Complex` to represent complex numbers and include methods and operator overloads for complex arithmetic:
  1. Constructor, with a default constructor that initializes the complex number to 0 + 0i.
  2. Overloaded `+` operator to add two complex numbers.
  3. Overloaded `*` operator to multiply two complex numbers.
  4. Overloaded `<<` and `>>` operators for input/output operations.
- **Features**:
  - **Constructor & Default Constructor**: Allows initializing complex numbers, with the default constructor setting the number to 0 + 0i.
  - **Operator Overloading**:
    - `+`: Adds two complex numbers by summing their real and imaginary parts.
    - `*`: Multiplies two complex numbers using complex multiplication rules.
    - `<<` and `>>`: Enables formatted display and input of complex numbers.
  - **Usage**: This class demonstrates operator overloading, encapsulation, and formatted I/O for complex number arithmetic.

### Assignment 2: Student Information System Database

- **Problem Statement**: Develop a database to store student information, including Name, Roll Number, Class, Division, Date of Birth, Blood Group, Contact Address, Telephone Number, and Driving License Number. Use various OOP concepts:
  - Constructors (default and copy), destructor, static member functions, friend classes, `this` pointer, inline code, and dynamic memory allocation with `new` and `delete`.
- **Features**:
  - **Student Data Structure**: Organizes and stores essential student data.
  - **Constructors & Destructor**: Manages initialization and destruction of objects, with a copy constructor to copy student details.
  - **Dynamic Memory Allocation**: Uses `new` and `delete` to manage memory for objects dynamically.
  - **Friend Class & Static Member Functions**: Allows data access across classes and shared functionality across instances.
  - **This Pointer**: Demonstrates use of `this` pointer for object reference.
  - **Usage**: This system highlights memory management, friend functions, and class pointers in C++.

### Assignment 3: Book Shop Inventory System

- **Problem Statement**: Create an inventory system for a bookshop to manage books by details such as author, title, price, publisher, and stock. When a customer requests a book, the system:
  - Searches by title and author.
  - Displays availability or an "out of stock" message.
  - If available, prompts for the required quantity and calculates the total cost.
- **Features**:
  - **Book Structure**: Stores details like author, title, price, publisher, and stock position.
  - **Search Functionality**: Checks if a book is available based on title and author.
  - **Stock and Cost Calculation**: Calculates and displays the cost of requested copies if in stock; otherwise, alerts the user about stock unavailability.
  - **Memory Management**: Uses dynamic memory allocation with `new` in the constructor.
  - **Usage**: This assignment emphasizes object-oriented modeling of an inventory system, search algorithms, and dynamic memory management.

### Assignment 4: File Input/Output

- **Problem Statement**: Implement a program that demonstrates file I/O operations:
  - Creates and writes data to an output file.
  - Closes the file and reopens it in input mode to read the data.
- **Features**:
  - **File Creation & Writing**: Writes data to an output file, saving information for persistence.
  - **File Reopening & Reading**: Reopens the file to read and display the stored data.
  - **Error Handling**: Ensures that file operations succeed with error checking.
  - **Usage**: This assignment provides practice with file handling in C++ and reinforces data persistence concepts.

### Assignment 5: Selection Sort Template

- **Problem Statement**: Create a function template for a selection sort algorithm. Write a program that:
  - Inputs, sorts, and outputs an integer array.
  - Inputs, sorts, and outputs a float array.
- **Features**:
  - **Template Function**: Generalizes the selection sort algorithm for any data type.
  - **Sorting Algorithm**: Implements selection sort, a basic sorting algorithm with O(n^2) time complexity.
  - **Array Sorting**: Demonstrates sorting of integer and float arrays without relying on specific data types.
  - **Usage**: This assignment illustrates the use of function templates for generic programming in C++.

### Assignment 6: STL Sorting and Searching

- **Problem Statement**: Use the Standard Template Library (STL) for sorting and searching custom records:
  - **Person Record**: Contains name, Date of Birth, and telephone number.
  - **Item Record**: Contains item code, name, cost, and quantity.
  - Use the `vector` container to store records.
- **Features**:
  - **Vector Container**: Stores and manages collections of person and item records.
  - **Sorting & Searching**: Demonstrates sorting and searching operations on custom data structures.
  - **STL Utilization**: Uses STL algorithms for efficiency and simplicity.
  - **Usage**: This assignment demonstrates the power of STL containers and algorithms to handle and process user-defined data types.

### Assignment 7: Map Associative Container for State Populations

- **Problem Statement**: Implement a program using the `map` associative container, where:
  - Keys represent state names.
  - Values represent state populations.
  - The program prompts the user to enter a state name and retrieves the population using the map.
- **Features**:
  - **Map Container**: Associates state names with populations for fast lookups.
  - **Key-Value Access**: Prompts user for a state name, retrieves, and displays population.
  - **Efficiency**: Demonstrates the efficiency of associative containers for key-value access.
  - **Usage**: This assignment highlights C++ map container operations, demonstrating associative container handling in C++.

---

Each assignment is contained within its respective folder. Open individual folders in Eclipse for a focused and organized development experience.

---
