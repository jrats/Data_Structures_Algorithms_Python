class StarCookie:
    milk = 0.2    #class attribute, same for all objects created from this class
    def __init__(self, color, weight=15):
        # print("The cookie is ready")            #will get printed everytime the object is created
        self.color = color
        self.weight = weight
                                            
star_cookie1 = StarCookie('Red')
star_cookie1.milk = 0.5   #overriding class variables

StarCookie.milk = 0.7

star_cookie2 = StarCookie('Blue', 16)
star_cookie1.flour = 'wheat'    #can still add additional attributes

print(star_cookie1.milk)     
print(star_cookie2.milk)
print(StarCookie.milk)      #all 3 will give 0.2, since milk is a class variable

print(star_cookie1.__dict__)
print(star_cookie2.__dict__)
print(StarCookie.__dict__)



print(star_cookie1.color)
print(star_cookie1.weight)
print(star_cookie1.flour)

# star_cookie1.weight = 15
# star_cookie1.color = "Red"
# print(star_cookie1.weight)
# print(star_cookie1.color)

# star_cookie2 = StarCookie()
# star_cookie2.weight = 30
# star_cookie2.color = "Blue"
# print(star_cookie2.weight)    # have to initliaise everytime
# print(star_cookie2.color)

class Youtube:
    def __init__(self, username, subscription=0, subscriber=0):
        self.username = username
        self.subscription = subscription
        self.subscriber = subscriber

    def subscribe(self,user):
        user.subscriber +=1
        self.subscription +=1

user1 = Youtube('Juhi')
user2 = Youtube('Nidhi')

user1.subscribe(user2)

print("Juhi subscriber :", user1.subscriber)
print("Juhi subscription :", user1.subscription)
print("Nidhi subscriber :", user2.subscriber)
print("Nidhi subscription :", user2.subscription)
        



