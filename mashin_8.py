class Vehicles:
    def __init__(self, name, capacity, place, wheels,  energy ):
        self.name= name
        self.capacity= capacity
        self.place= place
        self.wheels= wheels
        self.energy = energy


class Car(Vehicles):
    def __init__(self, name, capacity, place, wheels, energy, doors ):
        super().__init__(name, capacity, place, wheels,  energy )
        self.doors= doors


BMV= Car("BMV", 4, "the land", 4, "petrol", 4)

#print(bmv.energy)
class Airplane(Vehicles):
    def __init__(self, name, capacity, place, wheels, energy, wings ):
        super().__init__(name, capacity, place, wheels,  energy )
        self.wings=wings

Airbus= Airplane("Airbus", 400, "in the air", 22, "gasoline", 2)

class Motor(Vehicles):
    def __init__(self, name, capacity, place, wheels, energy ):
        super().__init__(name, capacity, place, wheels,  energy )

        def extra(self):
            print("use a helmet when you use the engine")

Yamaha= Motor("Yamaha", 2, "the land", 3, "petrol")


print("capacity is: ",Yamaha.capacity)
print("place of Airplane movement: ",Airbus.place)
print("the number of car doors:", BMV.doors)
print("number of airplanes wings: ",Airbus.wings)
