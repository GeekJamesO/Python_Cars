class Car():
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def get_tax(self):
        if self.price > 10000:
            return 0.15
        else:
            return 0.12
    def __str__(self):
        return "Price: ${} Speed: {}mph, Fuel: {}, Mileage: {}, Tax: {}%.".format(self.price, self.speed, self.fuel, self.mileage, self.get_tax() )

    def display_all(self):
        print "  Price:", self.price
        print "  Speed:", self.speed, "mph"
        print "  Fuel: Tank is", self.fuel
        print "  Mileage:", self.mileage, "mpg"
        print "  Tax:", self.get_tax()
        return self
print "The Car"
Olds = Car(101000, 60, "1/2 full", 45)
Olds.display_all()

print "the Childrens toy"
TonkaTruck = Car(20, 0, "plastic", 0)
TonkaTruck.display_all()
