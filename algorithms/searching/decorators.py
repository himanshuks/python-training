# Decorators are used to wrap a function using @
# This way we can add extra functionality to an existing function without touching it's code

import time

# Wrapper function created
# It take and return FUNCTION as argument
# First create a wrapper function
# Inside it create a nested function

# We have passed argument as FUNC
def cal_time(func):

    # *args -> means 'n' number of arguments can be passed
    # **kwargs -> means 'n' number of dictionary type key-value pairs can be passed
    def inner_wrap(*args, **kwargs):
        start = time.time()

        # Store and return passed FUNC with same arguments
        result = func(*args, **kwargs)

        end = time.time()

        # .__name__ -> Will returns the name of the function currently passed
        print(f"The function {func.__name__} took {(end-start)*1000} ms")
        return result

    # Simply return the nested function at the end
    return inner_wrap


# Use decorators with @
@cal_time
def cal_square(list):
    result = []
    for i in list:
        result.append(i * i)
    return result


@cal_time
def cal_cube(list):
    result = []
    for i in list:
        result.append(i * i * i)
    return result


number_list = range(1, 100000)
square = cal_square(number_list)
cube = cal_cube(number_list)
