students = [
    {
        'name': 'Alice',
        'age': 25,
        'major': 'Physics'
    },
    {
        'name': 'Bob',
        'age': 22,
        'major': 'Computer Science'
    },
    {
        'name': 'Charlie',
        'age': 23,
        'major': 'Mathematics'
    }
]
#accessing Data 
first_student_major = students[0]['major']
print(first_student_major)  # Output: Physics

# Looping through the list of students
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Expected Output:
# Name: Alice, Age: 25, Major: Physics
# Name: Bob, Age: 22, Major: Computer Science
# Name: Charlie, Age: 23, Major: Mathematics

# Accessing Alice's favorite books
alice_books = favorite_books['Alice']
print(alice_books)  # Output: ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice']

# Accessing Bob's second favorite book
second_favorite_bob = favorite_books['Bob'][1]
print(second_favorite_bob)  # Output: Catch-22

# Looping through each person and their list of favorite books
for person, books in favorite_books.items():
    print(f"{person}'s favorite books:")
    for book in books:
        print(f" - {book}")

# Expected Output:
# Alice's favorite books:
#  - 1984
#  - To Kill a Mockingbird
#  - Pride and Prejudice
# Bob's favorite books:
#  - The Great Gatsby
#  - Catch-22
#  - Moby Dick
# Charlie's favorite books:
#  - The Hobbit
#  - Harry Potter
#  - War and Peace