class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self._battery = None
        self.battery = battery  # uses setter for validation

    @property
    def battery(self):
        return self._battery
    
    @battery.setter
    def battery(self, value):
        if 0 <= value <= 100:
            self._battery = value
        elif value > 100:
            self._battery = 100
        else:
            raise ValueError("Battery must be between 0 and 100")
        
    def call(self, number, minutes=1):
        print(f"{self.brand} {self.model} calling {number} for {minutes} minute(s)...")
        self._drain(minutes)

    def charge(self, amount):
        print(f"Charging +{amount}%...")
        self.battery = self.battery + amount
        print(f"Battery is now {self.battery}%")

    def specs(self):
        return f"{self.brand} {self.model} | Battery: {self.battery}%"

    def _drain(self, amount):
        self.battery = max(0, self.battery - amount)


# Polymorphism Challenge
class Vehicle:
    def move(self):
        print("This vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Tests
if __name__ == "__main__":
    # Smartphone test
    phone1 = Smartphone("Samsung", "Galaxy S24", battery=60)
    print(phone1.specs())
    phone1.call("08012345678", minutes=5)
    phone1.charge(30)
    print(phone1.specs())


print("\n--- Using a Loop ---")
Vehicle = [Car(), Plane(), Boat()]
for v in Vehicle:
    v.move()