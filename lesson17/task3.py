class Fraction:

    def __init__(self, nom : int, denom : int):
        self.nom = nom
        self.denom = denom
    
    def __add__(self, another):
        a = self.nom
        x = self.denom
        b = another.nom
        y = another.denom
        if x == 0 or y == 0:
            return "Zero devision"
        else:
            if x == y:
                return Fraction(a + b, x)
            elif x > y:
                if x % y == 0:
                    return Fraction(a + b * (x // y), x)
                else:
                    return Fraction(a * y + b * x , x * y)
            else:
                if y % x == 0:
                    return Fraction(a * (y // x) + b, y)
                else:
                    return Fraction(a * y + b * x, x * y)
    
    def __sub__(self, another):
        a = self.nom
        x = self.denom
        b = another.nom
        y = another.denom
        if x == 0 or y == 0:
            return "Zero devision"
        else:
            if x == y:
                return Fraction(a - b, x)
            elif x > y:
                if x % y == 0:
                    return Fraction(a - b * (x // y), x)
                else:
                    return Fraction(a * y - b * x , x * y)
            else:
                if y % x == 0:
                    return Fraction(a * (y // x) - b, y)
                else:
                    return Fraction(a * y - b * x, x * y)
    
    def __mul__(self, another):
        a = self.nom
        x = self.denom
        b = another.nom
        y = another.denom
        if x == 0 or y == 0:
            return "Zero devision"
        else:
            return Fraction(a * b, x * y)
    
    def __truediv__(self, another):
        a = self.nom
        x = self.denom
        b = another.nom
        y = another.denom
        if x == 0 or y == 0 or b == 0:
            return "Zero devision"
        else:
            return Fraction(a * y, x * b)
    
    def __str__(self) -> str:
        if self.nom == 0:
            return "0"
        else:
            return f"{self.nom}\n--\n{self.denom}"

# x = Fraction(1, 2)
# y = Fraction(1, 2)
# rez1 = x + y
# print(str(rez1))
# rez2 = x - y
# print(str(rez2))
# rez3 = x * y
# print(str(rez3))
# rez4 = x / y
# print(str(rez4))

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)