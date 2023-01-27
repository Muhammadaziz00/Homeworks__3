# класс - тип, описывающий устройство объекта.

# class HelloWorld():
#     name = "Adilet"
#     age = 16

#     def walk(self):
#         return "Ходить"

#     def run(self):
#         return "Бегать"

#     def info(self):
#         return f"Имя: {self.name}, возраст: {self.age}"


# hello = HelloWorld()
# print(hello.info())
# print(hello.walk())
# print(hello.run())


# class Person():
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def walk(self):
#         return f"{self.name} гуляет"

#     def run(self):
#         return f"{self.name} бегает"

#     def info(self):
#         return f" Имя: {self.name}, фамилия: {self.surname}, возраст: {self.age}"

# a = Person("Aziz", "said", 16)
# print(a.info())
# print(a.walk())
# print(a.run())
# b = Person("Adilet", "Python",19)
# print(b.info())


class Car():
    def __init__(self, brand, mobel, year, color, type, volume):
        self.band = brand
        self.mobel = mobel
        self.year = year
        self.color = color
        self.type = type
        self.volume = volume
        self.odometer = 0
        self.is_going = False


    def info_car(self):
        return f"Brand: {self.band}, model: {self.mobel}, year: {self.year}, type: {self.type}, volume: {self.volume}, {self.odometer} km, status: {self.is_going}"


    # def start_engin

mersedes = Car("Mersedes", "W223", 2022, "White", "Sedan", 5.5)
print(mersedes.info_car())
    

