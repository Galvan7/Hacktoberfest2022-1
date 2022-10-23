class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2): #these are inbuilt dunders #OPERATOR OVERLOADING OTGHERS ARE __sub__,__truediv__,__muldiv__
        print("Lets multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sudfsm = n1 + n2
mul = n1 * n2
print(sudfsm)
print(mul)
