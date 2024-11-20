# Quiz App data saved in program memory


import random as ran

# User data and quiz questions
users = {}
quiz_questions = {
    "Python": [
        {"question": "What is the output of: print(2 ** 3)?", "choices": ["1. 6", "2. 9", "3. 8"], "answer": 3},
        {"question": "What is the correct file extension for Python files?", "choices": ["1. .pt", "2. .pyt", "3. .py"], "answer": 3},
        {"question": "Which function is used to get the length of a list?", "choices": ["1. size()", "2. len()", "3. count()"], "answer": 2},
        {"question": "Which of the following is immutable in Python?", "choices": ["1. List", "2. Dictionary", "3. Tuple"], "answer": 3},
        {"question": "How do you create a dictionary?", "choices": ["1. {}", "2. []", "3. ()"], "answer": 1},
        {"question": "Which of the following is used to define a function in Python?", "choices": ["1. function", "2. def", "3. lambda"], "answer": 2},
        {"question": "Which data type is mutable in Python?", "choices": ["1. Tuple", "2. List", "3. String"], "answer": 2},
        {"question": "What is the output of 'print(type(10))' in Python?", "choices": ["1. int", "2. float", "3. str"], "answer": 1},
        {"question": "How do you start a loop in Python?", "choices": ["1. for", "2. while", "3. loop"], "answer": 1},
        {"question": "What is the output of 'print(3 // 2)'?", "choices": ["1. 1", "2. 1.5", "3. 2"], "answer": 1},
        {"question": "What is the output of: print(2 ** 3)?", "choices": ["1. 6", "2. 9", "3. 8"], "answer": 3},
        {"question": "What is the correct file extension for Python files?", "choices": ["1. .pt", "2. .pyt", "3. .py"], "answer": 3},
        {"question": "Which function is used to get the length of a list?", "choices": ["1. size()", "2. len()", "3. count()"], "answer": 2},
        {"question": "Which of the following is immutable in Python?", "choices": ["1. List", "2. Dictionary", "3. Tuple"], "answer": 3},
        {"question": "How do you create a dictionary?", "choices": ["1. {}", "2. []", "3. ()"], "answer": 1},
        {"question": "What is the output of 'print(type(10))' in Python?", "choices": ["1. int", "2. float", "3. str"], "answer": 1},
        {"question": "What is the output of: print(bool([]))?", "choices": ["1. True", "2. False", "3. Error"], "answer": 2},
        {"question": "Which module is used for regular expressions in Python?", "choices": ["1. regex", "2. re", "3. match"], "answer": 2},
        {"question": "How do you handle exceptions in Python?", "choices": ["1. try...catch", "2. try...except", "3. try...handle"], "answer": 2},
    ],
    "DSA": [
        {"question": "What is the time complexity of binary search?", "choices": ["1. O(log n)", "2. O(n)", "3. O(n^2)"], "answer": 1},
        {"question": "Which data structure works on FIFO?", "choices": ["1. Stack", "2. Queue", "3. Tree"], "answer": 2},
        {"question": "What is the time complexity of merging two sorted arrays?", "choices": ["1. O(n)", "2. O(n^2)", "3. O(log n)"], "answer": 1},
        {"question": "Which sorting algorithm is considered stable?", "choices": ["1. Quick Sort", "2. Bubble Sort", "3. Merge Sort"], "answer": 3},
        {"question": "Which data structure is used to implement a priority queue?", "choices": ["1. Stack", "2. Binary Heap", "3. Linked List"], "answer": 2},
        {"question": "What is the time complexity of inserting an element in a linked list?", "choices": ["1. O(1)", "2. O(log n)", "3. O(n)"], "answer": 1},
        {"question": "What is the time complexity of binary search?", "choices": ["1. O(log n)", "2. O(n)", "3. O(n^2)"], "answer": 1},
        {"question": "Which data structure works on FIFO?", "choices": ["1. Stack", "2. Queue", "3. Tree"], "answer": 2},
        {"question": "Which is the best sorting algorithm in terms of time complexity?", "choices": ["1. Merge Sort", "2. Bubble Sort", "3. Selection Sort"], "answer": 1},
        {"question": "What is the worst-case time complexity of Quick Sort?", "choices": ["1. O(n log n)", "2. O(n^2)", "3. O(n)"], "answer": 2},
        {"question": "Which of the following uses a graph?", "choices": ["1. HashMap", "2. Binary Tree", "3. DFS"], "answer": 3},
        {"question": "What is the maximum number of nodes in a binary tree of height h?", "choices": ["1. 2^h", "2. 2^(h+1) - 1", "3. h^2"], "answer": 2},
        {"question": "What is the space complexity of BFS?", "choices": ["1. O(V + E)", "2. O(V)", "3. O(E)"], "answer": 1},
    ],
    "C++": [
        {"question": "Which of the following is a correct variable declaration in C++?", "choices": ["1. int num;", "2. num int;", "3. int: num"], "answer": 1},
        {"question": "What is the size of an integer in C++?", "choices": ["1. 2 bytes", "2. 4 bytes", "3. 8 bytes"], "answer": 2},
        {"question": "Which loop is guaranteed to execute at least once?", "choices": ["1. for", "2. while", "3. do-while"], "answer": 3},
        {"question": "What is the output of: cout << sizeof(char); ?", "choices": ["1. 1", "2. 2", "3. 4"], "answer": 1},
        {"question": "Which of the following is not a fundamental data type in C++?", "choices": ["1. int", "2. float", "3. String"], "answer": 3},
        {"question": "What is a correct syntax to create a pointer in C++?", "choices": ["1. int* ptr;", "2. int ptr*;", "3. pointer int ptr;"], "answer": 1},
        {"question": "Which of the following is a correct variable declaration in C++?", "choices": ["1. int num;", "2. num int;", "3. int: num"], "answer": 1},
        {"question": "What is the size of an integer in C++?", "choices": ["1. 2 bytes", "2. 4 bytes", "3. 8 bytes"], "answer": 2},
        {"question": "Which operator is used to access a member of a structure?", "choices": ["1. .", "2. ->", "3. :"], "answer": 1},
        {"question": "What is the default return type of a function?", "choices": ["1. void", "2. int", "3. float"], "answer": 2},
        {"question": "Which feature of OOP ensures private data is accessed through a function?", "choices": ["1. Abstraction", "2. Encapsulation", "3. Polymorphism"], "answer": 2},
        {"question": "Which loop is guaranteed to execute at least once?", "choices": ["1. for loop", "2. while loop", "3. do-while loop"], "answer": 3},
    ],
    "Java": [
        {"question": "Which keyword is used to inherit a class in Java?", "choices": ["1. implements", "2. extends", "3. inherits"], "answer": 2},
        {"question": "Which method is used to start a thread in Java?", "choices": ["1. run()", "2. execute()", "3. start()"], "answer": 3},
        {"question": "What is the default value of an int variable?", "choices": ["1. null", "2. 0", "3. undefined"], "answer": 2},
        {"question": "Which collection type does not allow duplicate elements?", "choices": ["1. List", "2. Set", "3. Map"], "answer": 2},
        {"question": "Which keyword is used to define a constant in Java?", "choices": ["1. static", "2. const", "3. final"], "answer": 3},
        {"question": "Which of the following is not a feature of Java?", "choices": ["1. Object-Oriented", "2. Platform Dependent", "3. Secure"], "answer": 2},
        {"question": "Which keyword is used to inherit a class in Java?", "choices": ["1. implements", "2. extends", "3. inherits"], "answer": 2},
        {"question": "Which method is used to start a thread in Java?", "choices": ["1. run()", "2. execute()", "3. start()"], "answer": 3},
        {"question": "What is the default value of an int variable?", "choices": ["1. null", "2. 0", "3. undefined"], "answer": 2},
        {"question": "Which collection type does not allow duplicate elements?", "choices": ["1. List", "2. Set", "3. Map"], "answer": 2},
        {"question": "Which of the following is not a feature of Java?", "choices": ["1. Object-Oriented", "2. Platform Dependent", "3. Secure"], "answer": 2},
        {"question": "What is used to handle exceptions in Java?", "choices": ["1. try-catch", "2. error handling", "3. throw-handler"], "answer": 1},
    ],
}

current_user = None
score = 0


def display_menu():
    print(
        """
        *******************************************************************************
                                    QUIZ APPLICATION
        *******************************************************************************
                    1. Register
                    2. View Users
                    3. Login
                    4. Attempt Quiz
                    5. View Result
                    6. Exit
        *******************************************************************************
        """
    )

def register_user():
    global users
    print("\n********** Register Yourself **********\n")
    username = input("Enter your username: ").upper()
    if username in users:
        print("\nYou are already registered!\n")
        return

    print("""
        Password Requirements:
        1. At least one lowercase letter
        2. At least one uppercase letter
        3. At least one digit
        4. Length between 8 to 20 characters
        5. At least one special character (@, #, %, _, $)
    """)
    while True:
        password = input("Enter your password: ")
        if validate_password(password):
            users[username] = password
            print("\nRegistration successful!\n")
            break
        else:
            print("Invalid password. Please follow the requirements.")

def validate_password(password):
    if 8 <= len(password) <= 20:
        l, u, d, s = 0, 0, 0, 0
        for char in password:
            if char.islower(): l += 1
            if char.isupper(): u += 1
            if char.isdigit(): d += 1
            if char in "@#%_$": s += 1
        return l >= 1 and u >= 1 and d >= 1 and s >= 1
    return False

def view_users():
    if users:
        print("\nRegistered Users:")
        for user in users:
            print(user)
    else:
        print("\nNo users registered yet.")

def login_user():
    global current_user
    print("\n********** Login **********\n")
    username = input("Enter your username: ").upper()
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        current_user = username
        print(f"\nLogin successful! Welcome, {username}.\n")
    else:
        print("\nInvalid username or password.\n")

def attempt_quiz():
    global score
    if not current_user:
        print("\nPlease log in to attempt the quiz.\n")
        return

    print("\nChoose a quiz category:")
    for i, category in enumerate(quiz_questions.keys(), start=1):
        print(f"{i}. {category}")
    
    while True:
        try:
            category_choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= category_choice <= len(quiz_questions):
                selected_category = list(quiz_questions.keys())[category_choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid category.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_questions = ran.sample(quiz_questions[selected_category], 5)
    score = 0
    print(f"\n{current_user}, let's start the quiz in the '{selected_category}' category!\n")
    
    for i, question in enumerate(selected_questions, start=1):
        print(f"Q{i}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        while True:
            try:
                answer = int(input("Choose the correct answer (1, 2, or 3): "))
                if answer in [1, 2, 3]:
                    break
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if answer == question['answer']:
            score += 1
    print("\nQuiz completed!")
    print(f"Check your result by selecting option 5.\n")


def view_result():
    if current_user:
        print(f"\n{current_user}'s Score: {score}/5\n")
    else:
        print("\nPlease log in and attempt the quiz first.\n")

# Main Program Loop
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        register_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        login_user()
    elif choice == '4':
        attempt_quiz()
    elif choice == '5':
        view_result()
    elif choice == '6':
        print("\nExiting the application. Goodbye Thank You!\n")
        break
    else:
        print("\nInvalid choice. Please try again.\n")
