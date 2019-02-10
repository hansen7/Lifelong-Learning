
import timeit
'''Interators'''
def check_prime(number):
    for divisor in range(2, int(number**0.5)+1):
        if number % divisor == 0:
            return False
    return True


class Primes:
    def __init__(self, max):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration # ends the iterator
        elif check_prime(self.number):
            return self.number # return prime number
        else:
            return self.__next__()



'''Generators'''
'''Generators introduce the yield statement to Python. 
It works a bit like return because it returns a value.
The difference is that it saves the state of the function. 
The next time the function is called, execution continues from where it left off, 
with the same variable values it had before yielding.'''
def Primes_gen(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number


if __name__ == '__main__':
    #timeit.timeit('initial_()', setup='number=100') 
    primes = Primes(100)
    print(primes)

    #for x in primes:
    #    print(x)