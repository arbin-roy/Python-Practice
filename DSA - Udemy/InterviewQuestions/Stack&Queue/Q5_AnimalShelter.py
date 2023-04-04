# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like. Create the data structures to maintain this system
# and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enQueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def deQueueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            return self.cats.pop(0)

    def deQueueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            return self.dogs.pop(0)

    def deQueueAny(self):
        if len(self.cats) == 0:
            return self.dogs.pop(0)
        else:
            return self.cats.pop(0)


shelterQ = AnimalShelter()
shelterQ.enQueue('Cat1', 'Cat')
shelterQ.enQueue('Cat2', 'Cat')
shelterQ.enQueue('Dog1', 'Dog')
shelterQ.enQueue('Cat3', 'Cat')
shelterQ.enQueue('Dog2', 'Dog')
print(shelterQ.deQueueDog())
