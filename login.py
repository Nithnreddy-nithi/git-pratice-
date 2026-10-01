class Person:
    name:str
    age:int

def login(person: Person):
    print(f"Logging in {person.name} who is {person.age} years old.")

def logout(person: Person):
    print(f"Logging out {person.name}.")
