class Caw():

    def makw_sound(self):
        return f"Myy! "

a = Caw()
print(a.makw_sound())
# ########################################

# class Cars():
#    brand = 'bmw'
#    model = 'e34'
#    year = 1998
#    odometr = 0
#    type_of = 'black'
#    volume = 5.5
#    is_going = False

#    def info_about_car(self.brand,):




class Cars():
    def __init__(self, brand, mobel, year, color, type_of, volume):
        self.band = brand
        self.mobel = mobel
        self.year = year
        # self.color = color
        # self.type_of = type_of
        # self.volume = volume
        # self.odometer = 0
        # self.is_going = False


    def info_car(self):
        return f"Brand: {self.band}, model: {self.mobel}, year: {self.year}"

    def car_is_going(self):
        self.is_going = True
        return f" {self.band} {self.model} Заведена"

    def drive(self, km):
        self.odometer += km
        return f"Проехал: "

b = Cars()
print(b.info_car(bmw, e34, 1998))
print(b.car_is_going())
print(b.drive(443))

