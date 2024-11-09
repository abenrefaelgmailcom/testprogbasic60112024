
# WRONG!! default x=1, y, z, df1 = 1, df2 = 2 ... -- WRONG!!
# default x, y, z, df1 = 1, df2 = 2 ... -- CORRECT!!
def my_mul(x: int = 1, y: int = 1):
    # x: int = 1
    # y: int = 2
    mul_x_y: int = x * y
    print(mul_x_y)
my_mul()
my_mul(3)
my_mul(y = 4)
my_mul(6, 19)
my_mul(x = 6, y = 19)

# create a divide function
# x : int , y: int default 1
# print x / y (only if y is not zero)
# call the function: my_div(10), my_div(10, 2), my_div (9, 4)
def my_div(x, y: int = 1):
    if y != 0:
        div_x_y: float = x / y
        print(div_x_y)
    else:
        print('cannot divide by zero')

my_div(10)
my_div(10, 2)
my_div(9, 4)
