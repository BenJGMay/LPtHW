## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has a init function that takes self and name. Below name attribute is set to name variable
        self.name = name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has a init function that takes self and name. Below name attribute is set to name variable
        self.name = name

## Person is an object
class Person(object):

        def __init__(self, name):
            ## Person has an init function that takes self and name self.name is set to name
            self.name = name

            ## Person has-a pet of some kind
            self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## calls the init of the parent class
        super(Employee, self).__init__(name)
        ## has-a salary set to the salary input
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class HAlibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has Satan as a pet
mary.pet = satan

## Frank is-an employee with 120,000 salary and is-a person
frank = Employee("Frank", 120000)

## Frank has rover as-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon and is-a Fish
crouse = Salmon()

## harry is-a Halibut and is-a Fish
harry = Halibut()
