import numpy as np

# in python, if an instance start 

class  Student(object):
    """docstring for  Student"""
    def __init__(self, name, score):
        super(Student, self).__init__()
        self.name = name
        self.__score = score # private attribute, which can not be directly reached from outside of the class


    '''to reach the private attribute of the object'''
    def get_score(self):
        return self.__score 

    '''to modify the private attribute of the object'''
    '''why using method instead of __init__? -> we can double check the input before modifying the attribute'''
    def set_score(self, score):
        #self.__score = score 
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Invalid Score Input') 


'''Here comes the inheritance of the class'''
class Animal(object):
    def run(self):
        print("Animal is running...")


class Dog(Animal):
    '''
    subclass of Animal, Animal is the superclass/base class of it
    when the method has the same name of the superclass method, if will run in this case
    '''
    #pass
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    pass

if __name__ == '__main__':
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()
