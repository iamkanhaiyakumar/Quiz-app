import mysql.connector
import random

# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",  # Replace with your MySQL username
    password="your_mysql_password",  # Replace with your MySQL password
    database="quiz_app"
)
cursor = db.cursor()

# Function to check if user exists
def check_user_exists(name):
    cursor.execute("SELECT id, password FROM users WHERE name = %s", (name,))
    result = cursor.fetchone()
    return result

# Function to add a new user
def add_new_user(name, password):
    cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
    db.commit()
    return cursor.lastrowid

# Function to save quiz score
def save_score(user_id, topic, score):
    cursor.execute("INSERT INTO scores (user_id, topic, score) VALUES (%s, %s, %s)", (user_id, topic, score))
    db.commit()

print("Hello User! This is a Quiz App")

# User login or registration
name = input("Enter your name: ")
user = check_user_exists(name)

if user:
    user_id, saved_password = user
    password = input("Enter your password: ")
    if password == saved_password:
        print("Login successful!")
    else:
        print("Incorrect password. Exiting.")
        exit()
else:
    password = input("Set a password you want: ")
    user_id = add_new_user(name, password)
    print("New user created successfully.")

# Questions for different topics
questions_python = [
    ("What is the output of print(2 ** 3)?", ["6", "8", "9", "5"], 2),
    ("Which data type is used for text?", ["int", "float", "str", "bool"], 3),
    ("What keyword is used to define a function?", ["def", "func", "define", "lambda"], 1),
    ("What is the default data type for numbers in Python?", ["int", "float", "double", "str"], 1),
    ("Which module is used for math operations?", ["sys", "math", "random", "os"], 2),
    ("What will be the output of print(10 // 3)?", ["3.33", "3", "3.0", "None"], 2),
    ("Which function is used to get the length of a list in Python?", ["size()", "length()", "len()", "count()"], 3),
    ("What is the output of print('Hello'[1])?", ["e", "H", "l", "o"], 1),
    ("Which of the following data types is immutable in Python?", ["list", "dict", "set", "tuple"], 4),
    ("Which keyword is used to start a function definition in Python?", ["func", "def", "function", "define"], 2),
    ("What is the output of print(5 % 2)?", ["0", "2", "1", "5"], 3),
    ("Which of the following methods is used to add an item to a list?", ["add()", "append()", "insert()", "extend()"],2),
    ("How do you start a comment in Python?", ["//", "/*", "#", "<!-- -->"], 3),
    ("What is the result of bool('') in Python?", ["True", "False", "1", "0"], 2),
    ("Which of the following is used to create a new set in Python?", ["[]", "{}", "()", "set()"], 4),
    ("Which method is used to convert a string to lowercase in Python?",["toLower()", "lowercase()", "lower()", "casefold()"], 3),
    ("What does range(5) produce in Python?",["[0, 1, 2, 3, 4]", "[1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4, 5]", "[1, 2, 3, 4]"], 1),
    ("Which of the following is a built-in Python data type?", ["stack", "queue", "dict", "graph"], 3),
    ("What is the correct syntax to check if a is equal to b in Python?", ["a = b", "a == b", "a eq b", "a != b"], 2),
    ("What is the output of print(type(5.0))?",["<class 'int'>", "<class 'float'>", "<class 'double'>", "<class 'decimal'>"], 2)
]

questions_cpp = [
    ("Which operator is used for insertion?", ["->", ">>", "<<", "::"], 3),
    ("How do you declare a constant variable?", ["const", "constant", "static", "define"], 1),
    ("What is used to terminate a statement?", [".", ":", ";", ","], 3),
    ("Which function returns the size of a data type?", ["sizeof", "length", "count", "size"], 1),
    ("Which of these is a logical operator?", ["&&", "+", "=", "*"], 1),
    ("Which operator is used to access members of a class through a pointer?", ["->", ".", "::", ":"], 1),
    ("What is the correct way to declare a constant variable in C++?", ["const int x = 10;", "constant int x = 10;", "int const x = 10;", "int constant x = 10;"], 1),
    ("Which loop structure is used to ensure the loop runs at least once?", ["for", "while", "do-while", "foreach"], 3),
    ("Which of the following is a correct way to allocate memory dynamically?", ["new int[10];", "alloc int[10];", "malloc(10);", "calloc(10);"], 1),
    ("Which of these is not a valid access modifier in C++?", ["public", "protected", "default", "private"], 3),
    ("What is the size of an int in C++ (assuming 32-bit architecture)?", ["2 bytes", "4 bytes", "8 bytes", "16 bytes"], 2),
    ("Which function is used to get the length of a string in C++?", ["length()", "size()", "strlen()", "Both length() and size()"], 4),
    ("Which of the following is used to terminate a statement in C++?", [";", ":", ".", ","], 1),
    ("Which function is used to get input from the user in C++?", ["cin", "cout", "scanf", "print"], 1),
    ("What does STL stand for in C++?", ["Standard Template Library", "Standard Type Library", "Standard Testing Library", "Simple Template Library"], 1),
    ("Which of the following is a feature of C++?", ["Object-oriented", "Procedural", "Functional", "All of the above"], 4),
    ("What is the output of 'cout << (5 > 3 ? 10 : 5);'?", ["5", "10", "3", "0"], 2),
    ("Which of the following is used to declare an array in C++?", ["int[] arr;", "array<int> arr;", "int arr[10];", "int arr{};"], 3),
    ("Which keyword is used to define a macro in C++?", ["macro", "define", "#define", "const"], 3),
    ("How do you declare a pointer in C++?", ["int *p;", "int p[];", "int &p;", "int p{};"], 1)
]

questions_java = [
    ("Java is platform-independent due to:", ["API", "JVM", "JRE", "JDK"], 2),
    ("Which keyword is used for inheritance?", ["inherits", "extends", "implements", "parent"], 2),
    ("What is the extension for compiled Java files?", [".jav", ".jv", ".class", ".java"], 3),
    ("Which is used for memory allocation?", ["malloc", "alloc", "new", "create"], 3),
    ("Java is:", ["Procedural", "Functional", "Scripting", "Object-Oriented"], 4),
    ("What is the size of an int data type in Java?", ["16-bit", "32-bit", "64-bit", "8-bit"], 2),
    ("Which of the following is not a Java keyword?", ["static", "public", "void", "integer"], 4),
    ("What is the purpose of the 'this' keyword in Java?",["Refers to current object", "Refers to parent class", "Refers to super class", "Refers to any class"], 1),
    ("Which method is called when an object is created in Java?", ["constructor", "method", "getter", "setter"], 1),
    ("What is the extension of a compiled Java class?", [".java", ".class", ".jav", ".byte"], 2),
    ("Which keyword is used for inheritance in Java?", ["inherits", "extends", "implements", "instanceof"], 2),
    ("What does JVM stand for?",["Java Variable Machine", "Java Virtual Machine", "Java Vector Machine", "Java Verification Machine"], 2),
    ("Which method can be used to find the length of a string in Java?", ["getSize()", "size()", "length()", "strlen()"],3),
    ("Which of these is not a feature of Java?",["Platform-Independent", "Object-Oriented", "Pointers", "Multithreading"], 3),
    ("Which keyword is used to create an interface in Java?", ["class", "extends", "interface", "implements"], 3),
    ("What is the default value of a boolean variable in Java?", ["true", "false", "1", "null"], 2),
    ("Which keyword in Java is used to handle exceptions?", ["try", "catch", "throw", "All of the above"], 4),
    ("Which of the following loops is entry-controlled?", ["do-while", "while", "for", "Both while and for"], 4),
    ("Which operator is used for bitwise AND in Java?", ["&", "|", "^", "%"], 1),
    ("How can you stop a loop in Java?", ["break", "return", "exit", "continue"], 1)
]

questions_dsa = [
    ("Which data structure follows LIFO?", ["Queue", "Stack", "Tree", "Graph"], 2),
    ("What is the time complexity of binary search?", ["O(n)", "O(log n)", "O(n^2)", "O(n log n)"], 2),
    ("Which is a linear data structure?", ["Graph", "Tree", "Stack", "Heap"], 3),
    ("Which sorting algorithm has the best average case performance?", ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort"], 2),
    ("What is the height of a balanced binary tree?", ["O(log n)", "O(n)", "O(n^2)", "O(1)"], 1),
    ("What is the size of an int data type in Java?", ["16-bit", "32-bit", "64-bit", "8-bit"], 2),
    ("Which of the following is not a Java keyword?", ["static", "public", "void", "integer"], 4),
    ("What is the purpose of the 'this' keyword in Java?",["Refers to current object", "Refers to parent class", "Refers to super class", "Refers to any class"], 1),
    ("Which method is called when an object is created in Java?", ["constructor", "method", "getter", "setter"], 1),
    ("What is the extension of a compiled Java class?", [".java", ".class", ".jav", ".byte"], 2),
    ("Which keyword is used for inheritance in Java?", ["inherits", "extends", "implements", "instanceof"], 2),
    ("What does JVM stand for?",["Java Variable Machine", "Java Virtual Machine", "Java Vector Machine", "Java Verification Machine"], 2),
    ("Which method can be used to find the length of a string in Java?", ["getSize()", "size()", "length()", "strlen()"],3),
    ("Which of these is not a feature of Java?",["Platform-Independent", "Object-Oriented", "Pointers", "Multithreading"], 3),
    ("Which keyword is used to create an interface in Java?", ["class", "extends", "interface", "implements"], 3),
    ("What is the default value of a boolean variable in Java?", ["true", "false", "1", "null"], 2),
    ("Which keyword in Java is used to handle exceptions?", ["try", "catch", "throw", "All of the above"], 4),
    ("Which of the following loops is entry-controlled?", ["do-while", "while", "for", "Both while and for"], 4),
    ("Which operator is used for bitwise AND in Java?", ["&", "|", "^", "%"], 1),
    ("How can you stop a loop in Java?", ["break", "return", "exit", "continue"], 1)
]

topics = {
    "1": ("Python", questions_python),
    "2": ("C++", questions_cpp),
    "3": ("Java", questions_java),
    "4": ("DSA", questions_dsa)
}

# Quiz Class
class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, min(5, len(questions)))  # Select 5 random questions
        self.answers = {}

    def take_quiz(self):
        for i, (question, options, correct_answer) in enumerate(self.questions, 1):
            print(f"Question {i}: {question}")
            for j, option in enumerate(options, 1):
                print(f"  {j}. {option}")
            answer = input("Select an option (1-4) or type 'mark' to attempt later: ")
            if answer.lower() == 'mark':
                self.answers[i] = None
            else:
                self.answers[i] = int(answer)

        # Revisit marked questions
        for i, (question, options, correct_answer) in enumerate(self.questions, 1):
            if self.answers[i] is None:
                print(f"\nMarked for Review - Question {i}: {question}")
                for j, option in enumerate(options, 1):
                    print(f"  {j}. {option}")
                answer = input("Select an option (1-4): ")
                self.answers[i] = int(answer)

    def calculate_score(self):
        score = 0
        for i, (_, _, correct_answer) in enumerate(self.questions, 1):
            if self.answers[i] == correct_answer:
                score += 1
        return score

# Main Quiz Loop
while True:
    print("\nSelect a topic for the quiz:")
    print("1. Python")
    print("2. C++")
    print("3. Java")
    print("4. DSA")
    topic_choice = input("Enter the number of your choice (or 'exit' to quit): ")

    if topic_choice.lower() == 'exit':
        print("Thank you for using the Quiz App. Goodbye!")
        break

    if topic_choice in topics:
        topic_name, questions = topics[topic_choice]
        print(f"\nStarting quiz on {topic_name}...\n")
        quiz = Quiz(questions)
        quiz.take_quiz()
        score = quiz.calculate_score()

        print(f"\nYour score: {score}/{len(quiz.questions)}")
        save_score(user_id, topic_name, score)
    else:
        print("Invalid choice. Please try again.")
