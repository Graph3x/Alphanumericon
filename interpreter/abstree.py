class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class String():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)


class Boolean():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return bool(self.value)

#TEMPLATE
class BinaryOperator():
    def __init__(self, left_var, right_var):
        self.left_var = left_var
        self.right_var = right_var


class Sum(BinaryOperator):
    def eval(self):
        return self.left_var.eval() + self.right_var.eval()


class Sub(BinaryOperator):
    def eval(self):
        return self.left_var.eval() - self.right_var.eval()


class Mul(BinaryOperator):
    def eval(self):
        return self.left_var.eval() * self.right_var.eval()


class Div(BinaryOperator):
    def eval(self):
        return self.left_var.eval() / self.right_var.eval()


class Equals(BinaryOperator):
    def eval(self):
        return self.left_var.eval() == self.right_var.eval()


class Bigger(BinaryOperator):
    def eval(self):
        return self.left_var.eval() > self.right_var.eval()


class Smaller(BinaryOperator):
    def eval(self):
        return self.left_var.eval() < self.right_var.eval()


class BiggerEqual(BinaryOperator):
    def eval(self):
        return self.left_var.eval() >= self.right_var.eval()


class SmallerEqual(BinaryOperator):
    def eval(self):
        return self.left_var.eval() <= self.right_var.eval()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())


class Input():
    def __init__(self):
        self.value = None

    def eval(self):
        self.value = input()
        return self.value


class Variable():
    def __init__(self, value, name):
        self.value = value
        self.name = name
    

class StringVar(Variable):
    def eval(self):
        return str(self.value)