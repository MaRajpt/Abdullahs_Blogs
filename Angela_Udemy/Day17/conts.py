###################################   CREATE CLASS ###############################
# first letter of class is capitalized

# class User:
#     pass
#
# user_1 = User()
# user_1.id = "001"
# user_1.name = "Sam"
#
# print(user_1.name)            THIS IS NOT A EFFICIENT WAY OF DOING THINGS (USER CONSTRUCTOR)

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1





user_1 = User("001", "Sam")
user_2 = User("002", "Kim")


user_1.follow(user_2)
user_2.follow(user_1)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)