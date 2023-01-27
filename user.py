class User:

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def say_hello(self):
        return f'Welcome {self.name}'
