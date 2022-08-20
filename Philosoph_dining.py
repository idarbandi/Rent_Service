from time import sleep
class Philosopher:
    guest_List = None
    forks = 0


    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.signin(self)
        self.forker()

    def __str__(self):
        print(f"Philosopher is {self.name}")






    def eat(self):
        print(f"Philosopher {self.name} is Eating")
        sleep(3)
        print(f"Philosopher {self.name} is Done Eating")




    def think(self):
        return f"Philosopher {self.name} is thinking"

    @classmethod
    def signin(cls, obj):
        if cls.guest_List == None:
            cls.guest_List = list()
        cls.guest_List.append(obj)


    @classmethod
    def BesmeLLah(cls):
        for gl in cls.guest_List:
            if cls.forks >= 2:
                cls.forks -= 2
                return gl.eat()
            return gl.think()

    @classmethod
    def forker(cls):
        cls.forks += 1

