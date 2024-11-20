import sqlite3
import bcrypt
import time

# Create the database and tables
def create_db():
    conn = sqlite3.connect("quiz_app.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        enrollment_number TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        correct_answer INTEGER NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        time_taken REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)
    conn.commit()
    conn.close()

# Insert sample questions
def insert_sample_questions():
    questions = [
        ("What is the output of: print(2 ** 3)?", "1. 6", "2. 9", "3. 8", 3),
        ("What is the correct file extension for Python files?", "1. .pt", "2. .pyt", "3. .py", 3),
        ("Which function is used to get the length of a list?", "1. size()", "2. len()", "3. count()", 2),
    ]
    conn = sqlite3.connect("quiz_app.db")
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO questions (question_text, option1, option2, option3, correct_answer)
    VALUES (?, ?, ?, ?, ?)
    """, questions)
    conn.commit()
    conn.close()

# Register new user
def register_user():
    print("\n******************** Register a New User ********************")
    name = input("Enter your name: ")
    enrollment_number = input("Enter your enrollment number: ")
    email = input("Enter your email: ")

    password = input("Enter your password: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    conn = sqlite3.connect("quiz_app.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO users (name, enrollment_number, email, password)
    VALUES (?, ?, ?, ?)
    """, (name, enrollment_number, email, hashed_password.decode('utf-8')))
    conn.commit()
    conn.close()
    print("Registration successful!\n")

# Login user
def login_user():
    print("\n******************** Login ********************")
    enrollment_number = input("Enter your enrollment number: ")
    password = input("Enter your password: ")

    conn = sqlite3.connect("quiz_app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE enrollment_number = ?", (enrollment_number,))
    user = cursor.fetchone()
    conn.close()

    if user:
        stored_password = user[4]  # Password is the 5th column in the 'users' table
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print("Login successful!\n")
            return user[0]  # Return user id for further use
        else:
            print("Incorrect password!\n")
            return None
    else:
        print("User not found!\n")
        return None

# Load questions from the database
def load_questions():
    conn = sqlite3.connect("quiz_app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    conn.close()

    questions = []
    for row in rows:
        question_text = row[1]
        options = [row[2], row[3], row[4]]
        correct_answer = row[5]
        questions.append((question_text, options, correct_answer))
    
    return questions

# Save quiz results
def save_results(user_id, score, time_taken):
    conn = sqlite3.connect("quiz_app.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO results (user_id, score, time_taken)
    VALUES (?, ?, ?)
    """, (user_id, score, time_taken))
    conn.commit()
    conn.close()

# Take the quiz
def take_quiz(user_id):
    print("\nStarting the quiz...\n")
    questions = load_questions()
    score = 0
    start_time = time.time()

    # Loop through each question
    for idx, (question_text, options, correct_answer) in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {question_text}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        # Get user input
        try:
            user_answer = int(input("Enter your answer (1/2/3): "))
        except ValueError:
            print("Invalid input, please enter 1, 2, or 3.")
            continue

        # Check the answer
        if user_answer == correct_answer:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"\nYour final score is {score}/{len(questions)}")
    print(f"Time taken: {time_taken:.2f} seconds")

    save_results(user_id, score, time_taken)
    print("\nYour results have been saved!\n")

# Main program
def main():
    create_db()  # Ensure database is created
    # Uncomment below to insert sample questions
    # insert_sample_questions()

    print("Welcome to the Quiz Application!")

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            user_id = login_user()
            if user_id:
                while True:
                    print("\n1. Take Quiz\n2. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        take_quiz(user_id)
                    elif user_choice == '2':
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice, please try again.")
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
