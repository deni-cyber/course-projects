class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_percent=100):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.__battery_percent = battery_percent  

    def charge(self):
        self.__battery_percent = 100
        print(f"{self.brand} {self.model} is now fully charged!")

    def use(self, percent):
        if self.__battery_percent - percent >= 0:
            self.__battery_percent -= percent
            print(f"Used {percent}% battery. Remaining: {self.__battery_percent}%")
        else:
            print("Not enough battery. Please charge the phone.")

    def battery_status(self):
        return f"Battery: {self.__battery_percent}%"

    def info(self):
        return f"{self.brand} {self.model}, {self.storage_gb}GB Storage"

# inheriting class
class GamingPhone(Smartphone):
    def use(self, percent):
        print("Launching Game Mode... ")
        super().use(percent + 10)  # Games tend to use more battery!

print("Smartphone Demo")
phone1 = Smartphone("Samsung", "Galaxy A50", 128)
print(phone1.info())
phone1.use(30)
print(phone1.battery_status())
phone1.charge()

gaming_phone = GamingPhone("ASUS", "ROG Phone 5", 256)
print(gaming_phone.info())
gaming_phone.use(30)
print(gaming_phone.battery_status())


# Assignment 2
class Vehicle:
    def move(self):
        raise NotImplementedError("Each vehicle must define its move method.")


class Car(Vehicle):
    def move(self):
        print("Driving ")


class Plane(Vehicle):
    def move(self):
        print("Flying")


class Boat(Vehicle):
    def move(self):
        print("Sailing")


class Train(Vehicle):
    def move(self):
        print("Rumbling along the tracks")


print("\n Polymorphism Demo")
vehicles = [Car(), Plane(), Boat(), Train()]
for v in vehicles:
    v.move()
