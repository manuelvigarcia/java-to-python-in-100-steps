class Country:
    def __init__(self, name):
        self.name = name
        print('constructor')

    def instance_method(self):
        print('instance method')

spain = Country("España")
spain.instance_method()

print(spain.name)