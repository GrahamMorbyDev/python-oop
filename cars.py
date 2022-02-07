class Car:
    # class attributes
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, model, year, make='Ford'):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.is_moving = False

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def __eg__(self, other):
        return self.make and self.model == other.model

    def stop(self):
        if self.is_moving:
            print('Car has stopped')
        else:
            print('The car is not moving')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('The car is moving')
                self.is_moving = True
            print(f'The car is going {speed}')
        else:
            print('You have run out of gas')
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True


class Dealership:
    def __init__(self):
        self.cars = []

    def __iter__(self):
        yield from self.cars

    def add_cars(self, car):
        self.cars.append(car)


car_one = Car('Focus', 2021)
car_two = Car('Focus', 2003,)
car_three = Car('Civic', 2010, 'Honda')

my_dealership = Dealership()
my_dealership.add_cars(car_one)
my_dealership.add_cars(car_two)
my_dealership.add_cars(car_three)

for car in my_dealership:
    print(car)

if car_one == car_two:
    print('equal')
else:
    print('Not equal')

