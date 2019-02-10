'''You can define functions inside functions'''
def hi(name="hansen"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


'''functions can also return a function'''
def hi_new(name="hansen"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "hansen":
        return greet
    else:
        return welcome


'''Now it comes for the decorator'''
from functools import wraps

def decorator_name(f):
    @wraps(f) # if not use wraps, then the function will change into decorated
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return ('Function is Running')


'''Decorator Usage Scenario -> Authorization'''
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated


'''Decorator Usage Scenario -> Logging'''
def logit(func): # logging while the function has been called
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + ' was called')
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x

'''There are also ways to build the decorators from the Class instead of functions'''
class logit(object):
    def __init__(self, logfile=r'./out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func) # keep the original attr of the func
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + ' was called'
            print(log_string)
            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        pass


class email_logit(logit):
    def __init__(self, email='hc.wang96@gmail.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        pass


if __name__ == '__main__':
    #hi()
    '''
    a = hi_new()
    print(a)
    print(a())'''
    #can_run = False
    #print(func())
    print(addition_func(4))