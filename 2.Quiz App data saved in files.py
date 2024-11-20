import os
import bcrypt
import time
import re  # Import regular expressions module
import random  # Importing the random module for randomizing questions

# Function to validate email
def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zAZ0-9-]+\.[a-zA0-9-.]+$'
    return re.match(email_pattern, email)

# Function to validate password
def is_valid_password(password):
    if (len(password) >= 8 and len(password) <= 20 and 
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'\d', password) and
        re.search(r'[@#%_$]', password)):
        return True
    return False

# Ensure the necessary files exist
def create_files():
    if not os.path.exists("users.txt"):
        open("users.txt", "w").close()  # Create the file if it doesn't exist
    if not os.path.exists("questions.txt"):
        with open("questions.txt", "w") as file:
            file.write("What is the output of: print(2 ** 3)?\n1. 6\n2. 9\n3. 8\nAnswer: 3\n")
            file.write("What is the output of: print(2 ** 3)?\n1. 6\n2. 9\n3. 8\nAnswer: 3\n")
            file.write("What is the correct file extension for Python files?\n1. .pt\n2. .pyt\n3. .py\nAnswer: 3\n")
            file.write("Which function is used to get the length of a list?\n1. size()\n2. len()\n3. count()\nAnswer: 2\n")
            file.write("Which of the following is immutable in Python?\n1. List\n2. Dictionary\n3. Tuple\nAnswer: 3\n")
            file.write("How do you create a dictionary?\n1. {}\n2. []\n3. ()\nAnswer: 1\n")
            file.write("Which of the following is used to define a function in Python?\n1. function\n2. def\n3. lambda\nAnswer: 2\n")
            file.write("Which data type is mutable in Python?\n1. Tuple\n2. List\n3. String\nAnswer: 2\n")
            file.write("What is the output of 'print(type(10))' in Python?\n1. int\n2. float\n3. str\nAnswer: 1\n")
            file.write("How do you start a loop in Python?\n1. for\n2. while\n3. loop\nAnswer: 1\n")
            file.write("What is the output of 'print(3 // 2)?'\n1. 1\n2. 1.5\n3. 2\nAnswer: 1\n")
            file.write("What is the output of: print(bool([]))?\n1. True\n2. False\n3. Error\nAnswer: 2\n")
            file.write("Which module is used for regular expressions in Python?\n1. regex\n2. re\n3. match\nAnswer: 2\n")
            file.write("How do you handle exceptions in Python?\n1. try...catch\n2. try...except\n3. try...handle\nAnswer: 2\n")
            file.write("What is the time complexity of binary search?\n1. O(log n)\n2. O(n)\n3. O(n^2)\nAnswer: 1\n")
            file.write("Which data structure works on FIFO?\n1. Stack\n2. Queue\n3. Tree\nAnswer: 2\n")
            file.write("What is the time complexity of merging two sorted arrays?\n1. O(n)\n2. O(n^2)\n3. O(log n)\nAnswer: 1\n")
            file.write("Which sorting algorithm is considered stable?\n1. Quick Sort\n2. Bubble Sort\n3. Merge Sort\nAnswer: 3\n")
            file.write("Which data structure is used to implement a priority queue?\n1. Stack\n2. Binary Heap\n3. Linked List\nAnswer: 2\n")
            file.write("What is the time complexity of inserting an element in a linked list?\n1. O(1)\n2. O(log n)\n3. O(n)\nAnswer: 1\n")
            file.write("Which is the best sorting algorithm in terms of time complexity?\n1. Merge Sort\n2. Bubble Sort\n3. Selection Sort\nAnswer: 1\n")
            file.write("What is the worst-case time complexity of Quick Sort?\n1. O(n log n)\n2. O(n^2)\n3. O(n)\nAnswer: 2\n")
            file.write("Which of the following uses a graph?\n1. HashMap\n2. Binary Tree\n3. DFS\nAnswer: 3\n")
            file.write("What is the maximum number of nodes in a binary tree of height h?\n1. 2^h\n2. 2^(h+1) - 1\n3. h^2\nAnswer: 2\n")
            file.write("What is the space complexity of BFS?\n1. O(V + E)\n2. O(V)\n3. O(E)\nAnswer: 1\n")

    if not os.path.exists("results.txt"):
        open("results.txt", "w").close()  # Create the results file if it doesn't exist

# Function for user registration
def register_user():
    print("\n******************** Register a New User ********************")
    name = input("Enter your name: ")
    enrollment_number = input("Enter your enrollment number: ")
    email = input("Enter your email: ")

    if not is_valid_email(email):
        print("Invalid email format. Please enter a valid email address.\n")
        return
    
    password = input("Enter your password: ")

    if not is_valid_password(password):
        print("Password does not meet the requirements.\n")
        return

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    with open("users.txt", "a") as file:
        file.write(f"{name},{enrollment_number},{email},{hashed_password.decode('utf-8')}\n")
    print("Registration successful!\n")

# Function for user login
def login_user():
    print("\n******************** Login ********************")
    enrollment_number = input("Enter your enrollment number: ")
    password = input("Enter your password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        user_details = user.strip().split(",")
        if user_details[1] == enrollment_number:
            if bcrypt.checkpw(password.encode('utf-8'), user_details[3].encode('utf-8')):
                print("Login successful!\n")
                return user_details[1]  # Return enrollment number as user identifier
            else:
                print("Incorrect password!\n")
                return None
    print("User not found!\n")
    return None

# Function to load questions properly and ensure options are correct
def load_questions():
    with open("questions.txt", "r") as file:
        lines = file.readlines()

    questions = []
    i = 0
    while i < len(lines):
        question_text = lines[i].strip()
        options = [lines[i+1].strip(), lines[i+2].strip(), lines[i+3].strip()]
        correct_answer = lines[i+4].strip().split(": ")[1]
        questions.append((question_text, options, correct_answer))
        i += 5
    return questions

# Function to administer the quiz (modified to limit to 10 questions and disable option shuffling)
def take_quiz(user_enrollment_number):
    questions = load_questions()
    random.shuffle(questions)
    
    # Limit to 10 questions
    questions_to_ask = questions[:10]
    
    score = 0
    start_time = time.time()

    print("\n******************** Starting the Quiz ********************")
    
    for idx, (question, options, correct_answer) in enumerate(questions_to_ask):
        print(f"\nQ: {question}")  # Removed the question number

        # No shuffling of options, display as is
        for option in options:
            print(option)
        
        user_answer = input("Your answer: ")
        
        # Validate answer input
        while user_answer not in ['1', '2', '3']:
            print("Invalid choice! Please enter 1, 2, or 3.")
            user_answer = input("Your answer: ")
        
        # Check if the answer is correct
        if options[int(user_answer)-1] == correct_answer:
            score += 1

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"\nQuiz completed! You scored {score}/{len(questions_to_ask)} in {time_taken:.2f} seconds.\n")

    # Store the result in results.txt
    with open("results.txt", "a") as file:
        file.write(f"Enrollment Number: {user_enrollment_number}, Score: {score}/{len(questions_to_ask)}, Time: {time_taken:.2f} seconds\n")

# Function to view results
def view_results(user_enrollment_number):
    print("\n******************** Your Quiz Results ********************")
    with open("results.txt", "r") as file:
        results = file.readlines()

    for result in results:
        if user_enrollment_number in result:
            print(result.strip())

# Main function to drive the program
def main():
    create_files()  # Ensure necessary files are created
    current_user = None
    while True:
        print("""
        *******************************************************************************
                                      QUIZ APPLICATION
        *******************************************************************************
                        1. Register (New User)
                        2. View Users
                        3. Login (Existing User)
                        4. Attempt Quiz
                        5. View Result
                        6. Exit
        *******************************************************************************
        """)
        choice = input("Enter your choice: ")

        # Validate menu choice
        while choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice! Please choose a valid option (1-6).")
            choice = input("Enter your choice: ")

        if choice == "1":  # New User (Registration)
            register_user()
        elif choice == "2":  # View Users
            with open("users.txt", "r") as file:
                users = file.readlines()
            print("\nList of Users:")
            for user in users:
                print(user.strip())
        elif choice == "3":  # Existing User (Login)
            current_user = login_user()
            if current_user:
                print(f"Welcome, {current_user}!")
            else:
                print("Login failed. Please try again.")
        elif choice == "4":  # Attempt Quiz
            if current_user:
                take_quiz(current_user)
            else:
                print("Please login first.")
        elif choice == "5":  # View Result
            if current_user:
                view_results(current_user)
            else:
                print("Please login first.")
        elif choice == "6":  # Exit
            print("Goodbye! Thank you for using the Quiz Application.\n")
            break

# Run the main function
if __name__ == "__main__":
    main()
