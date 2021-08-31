class Animal:
    def __init__(self):
        self.num_eyes = 2

        def breathe(self):
            print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        # This inherit all from the animal
        super().__init__()

    def swim(self):
        print("swim")

    def breathe(self):
        super().breathe()
        print("Doing this underwater")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)