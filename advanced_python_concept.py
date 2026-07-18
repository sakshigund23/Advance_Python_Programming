#generators program
def countdown(n):
    while n>0:
        yield n
        n -=1

#using generator
for num in countdown(5):
    print(num)

#output
#5
#4
#3
#2
#1


#iterators program
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#output
#1
#2
#3


#decorators program
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()

#output

#Something is happening before the function is called
#Hello!
#something is happening after the function is called