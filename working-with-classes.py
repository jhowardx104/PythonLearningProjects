class User:
    def __init__(self, username, age):
        self._username = username
        self._age = age

    def get_username(self):
        return self._username

    def set_username(self, value):
        self._username = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    def greet(self):
        print("Hello, %s - age %d!" % (self.get_username(), self.get_age()))

    def login(self, username, age):
        self.set_username(username)
        self.set_age(age)


loggedInUser = User("Jake", 32)
loggedInUser.greet()
loggedInUser.login("Mariah", 30)
loggedInUser.greet()
loggedInUser.set_username("Loki")
loggedInUser.set_age(5)
loggedInUser.greet()
loggedInUser.login("Ghost", 5)
loggedInUser.greet()