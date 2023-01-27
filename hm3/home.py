class Bank:
    def __init__(self, name, balanse):
        self.name = name 
        self.balanse = balanse

    def moneyX(self):
        user = int(input("Сколько вы хотите положить : "))
        self.balanse += user 
        return f"на вашем счету: {self.balanse}, Имя пользователя: {self.name}"

    def kill(self):
        user = int(input("сколько вы хотите обноличить: "))
        if user <= 0:
            self.balanse -= user 
            return f"на вашем счету: {self.balanse}"
        else:
            return f" на вешем счету не хватает денег {self.balanse}"

    def __jackpot(self):
        return f"ваш счет умножен 10р {self.balanse * 10}"


    def aza(self,name,balane):
        self.name = name
        self.balane = balane
        return f"Имя: {self.name}, Balanse: {self.balanse + self.balance}"

b = Bank('aza',180000)
print(b.moneyX())
print(b.kill())
print(b.aza("bekbolot", 100))
print(b.__jackpot())


class Calculator:
    def init(self, num):
        self.num = num

    def add(self, other):
        print("Сложение")
        return self.num + other.num

    def sub(self, other):
        print("Вычитание")
        return self.num - other.num

    def mul(self, other):
        print("Умножение")
        return self.num * other.num

    def truediv(self, other):
        print("Деление")
        return self.num / other.num
a = Calculator(1500)
b = Calculator(1240)
print(a + b)
print(a - b)
print(a * b)
print(a / b)