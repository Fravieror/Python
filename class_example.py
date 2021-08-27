# REQUIREMENTS: To do not generate errors a class need have at least something inside,
# can be one variable or one method ot you can simply use pass
# NAMING class: The first letter of each word must be capitalized (pascal) "PascalCase"
# note: (camel) case is after the second word "camelCase"
class User:
    # pass: pass to the next line of code, It does not do anything
    pass

    # constructor it is called every time that the object is created
    def __init__(self, user_id, username):
        # self: actual object that is being created
        self.id = user_id
        self.username = username
        # setting default value
        self.followers = 0
        self.following = 0
        print("new user benign created...")

    #  every method need as first parameter self it means that it method know the method that called it.
    def follow(self, user):
        user.followers += 1
        # it modifies the class that call it
        self.following += 1


user_1 = User("001", "angela")
# # adding an attribute
# user_1.id = "001"
# user_1.username = "angela"

print(user_1.username)

user_2 = User("002", "Javier")
# # For error is possible create different name to attributes, for this reason exists the constructor
# user_2.id = "002"
# user_2.username = "Javier"

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)