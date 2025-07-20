class Bird():

    def walk(self):
        print('Hoppping around.....')

class Mammal():

    def walk(self):
        print('Jogging around...')

class Movements:

    @classmethod
    def move(self,thing):
        thing.walk()


bird=Bird()
dog=Mammal()

Movements.move(bird)
Movements.move(dog)