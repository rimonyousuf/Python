class Phone:
    def __init__(self):
        print("I am in Phone class")

class Nokia(Phone):
    def __init__(self):
        super().__init__()
        print("I am in Nokia class")

n=Nokia()