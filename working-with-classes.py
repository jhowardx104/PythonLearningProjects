from modules import user
# see /modules/user.py for an example class definition
loggedInUser = user.User("Jake", 32)
loggedInUser.greet()
loggedInUser.login("Mariah", 30)
loggedInUser.greet()
loggedInUser.set_username("Loki")
loggedInUser.set_age(5)
loggedInUser.greet()
loggedInUser.login("Ghost", 5)
loggedInUser.greet()