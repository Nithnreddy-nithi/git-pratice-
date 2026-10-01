def add(a: int, b: int) -> int:
    res=a+b
    res1=a*b

    return res ,res1
class Vehicle():
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def vehicle_info(self):
        return f"Vehicle Name: {self.name}, Max Speed: {self.max_speed}, Mileage: {self.mileage}"
class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, seating_capacity):
        super().__init__(name, max_speed, mileage)
        self.seating_capacity = seating_capacity

    def vehicle_info(self):
        return f"Car Name: {self.name}, Max Speed: {self.max_speed}, Mileage: {self.mileage}, Seating Capacity: {self.seating_capacity}"
