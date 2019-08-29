# using utf-8
import logging


# logging records, then call the function
# the classic method is like this
def use_logging(func):
    logging.warn('%s is running'%func.__name__)
    fun()

def foo():
    print('I am foo')

# using decorator for the same function is like this
def use_logging_decorator(func):

    def wrapper():
        logging.warn('%s is running'%func.__name__)
        return func() # when pass the variable foo inside, execute func() 

    return wrapper

def foo():
    print('I am foo')

foo = use_logging_decorator(foo) # foo = wrapper
foo() # execute wrapper()


'''syntactic sugar'''
@use_logging_decorator # == 'foo=use_logging(foo)'
foo() # realize same function as above


'''func with arguments'''
def foo(name, age=None, height=None):
    print("I am %s, age %s, height %s" % (name, age, height))

def use_logging_decorator(func):

    def wrapper(*args, **kwargs):
        logging.warn('%s is running'%func.__name__)
        return func(*args, **kwargs) # when pass the variable foo inside, execute func() 

    return wrapper


'''decorators with arguments'''



if __name__ == '__main__':
    use_logging(foo)
