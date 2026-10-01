class Person:
    name:str
    age:int

def login(person: Person):
    print(f"Logging in {person.name} who is {person.age} years old.")
    