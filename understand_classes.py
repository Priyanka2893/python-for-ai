class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

tom = Dog("Tom", "Labrador")
print(tom.name)  # Output: Tom
print(tom.breed)  # Output: Labrador
print(tom.bark())  # Output: Woof!
class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Pass name to parent's __init__
        self.breed = breed      # Dog-specific attribute
    
    def describe(self):
        return f"{self.name} is a {self.breed}"

# Create dogs with breeds - positional arguments
golden = Dog("Buddy", "Golden Retriever")

# Or with named arguments (clearer)
poodle = Dog(name="Max", breed="Poodle")

print(golden.describe())  # Buddy is a Golden Retriever
print(golden.is_pet)      # True (inherited from Animal)

