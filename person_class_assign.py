class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        # Method to greet the person
    def greet(self):
        return f"Hello, my name is {self.name}!" 
      
        # Method to imulate a birthday
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old."
# Create instances of the Person class
person1 = Person("Alice", 30)                           
person2 = Person("Bob", 25)

# Use the methods of the Person class
print(person1.greet())  # Output: Hello, my name is Alice!
print(person2.have_birthday())  # Output: Happy birthday Bob! You are now 26 years old.
print(person1.age)  # Output: 30    