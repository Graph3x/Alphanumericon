from llvmlite import ir


class Number():
    def __init__(self, builder, module, value):
        self.value = value
        self.builder = builder
        self.module = module
    
    def eval(self):
        return ir.Constant(ir.IntType(8), int(self.value))
    
#TEMPLATE
class BinaryOperator():
    def __init__(self, builder, module, left_var, right_var):
        self.module = module
        self.builder = builder
        self.left_var = left_var
        self.right_var = right_var


class Sum(BinaryOperator):
    def eval(self):
        output = self.builder.add(self.right_var.eval(), self.left_var.eval())
        return output


class Sub(BinaryOperator):
    def eval(self):
        output = self.builder.sub(self.left_var.eval(), self.right_var.eval())
        return output


class Print():
    def __init__(self, builder, module, printf, value):
        self.value = value
        self.module = module
        self.builder = builder
        self.printf = printf

    def eval(self):
        value = self.value.eval()
        pointer_integer = ir.IntType(8).as_pointer()
        
        my_format = "%i \n\0"
        constant_format = ir.Constant(ir.ArrayType(ir.IntType(8), len(my_format)),bytearray(my_format.encode('utf-8')))

        global_format = ir.GlobalVariable(self.module, constant_format.type, name="format_string")
        global_format.linkage = 'internal'
        global_format.global_constant = True
        global_format.initializer = constant_format
        format_arg = self.builder.bitcast(global_format, pointer_integer)

        self.builder.call(self.printf, [format_arg, value])
