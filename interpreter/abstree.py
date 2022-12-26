class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

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


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())