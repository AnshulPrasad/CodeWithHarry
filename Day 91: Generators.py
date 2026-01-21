# store information to generate value and generate values when called using next()
# It saves computation and memory
# generators are lazy

def my_generator():
    for i in range(10):
        yield i


gen = my_generator()
print(next(gen))
print(next(gen))
