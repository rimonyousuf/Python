#parent class/Super class
#child class/sub class

class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

class Nokia(Phone):
    def pic(self):
        print("You can take photo")

n=Nokia()
n.call()
n.message()
n.pic()
print(issubclass(Nokia,Phone))
print(issubclass(Phone,Nokia))