
# return function within another function 
def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_num(100)

print("10 * 10 = ", generated_func(10)) # prints 1000

