# import a custom module
from modules.user import User
myUser = User("Jake", 32)
myUser.greet()

# working with built-in modules
import urllib.request

req = urllib.request.urlopen("https://facebook.com")
print(req.read())

# get docs on a lib/module
help(urllib.request)
