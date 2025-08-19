import heroes
# from turtle import Turtle, Screen
#
#
# #Object = Class
# jenny = Turtle()
# jenny.shape("turtle")
# jenny.color("DeepPink")
# jenny.fillcolor("chartreuse")
# jenny.position()
# jenny.forward(100)
# jenny.right(100)
# jenny.forward(100)
# jenny.left(100)
# jenny.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name",
#                  ["Pikachu", "Squirtle", "Carmander"])
# table.add_column("Type",
#                  ["Electric", "Fire", "Water"])
# table.align = "l"
# print(table)


# class User:
#     def __init__(self, user_id,username):
#         #Attributes
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0

#     #Methods
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1





# user_1 = User("001", " adriana")
# user_2 = User("002", "Antonio")

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person1 = Person("Adriana", 39)

# print(person1.name)
# print(person1.age)



# class House:

#     def __init__(self, wall_area):
#         self.wall_area = wall_area

#     def paint_needed(self):
#         return self.wall_area * 2.5
       
        
# class Paint:

#     def __init__(self, buckets, color):
#         self.color = color
#         self.buckets = buckets
        
#     def total_price(self):
#         if self.color == "white":
#             price = 1.99
            
#         else:
#             price = 2.19
        
        
#         return self.buckets * price
    
# from turtle import Turtle, Screen

# t = Turtle()
# t.shape("turtle")
# t.penup()
# t.goto(0, 50)


# t.pendown()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.right(90)
# t.backward(100)
# t.right(90)
# t.forward(100)



# Screen().exitonclick()


# class Paint:

#     def __init__(self, buckets, color): # Or get house area and height
#         self.color = color
#         self.buckets = buckets

#     def total_price(self):
#         if self.color == "white":
#             return self.buckets * 1.99
#         else:
#             return self.buckets * 2.19
            
            
# class DiscountedPaint(Paint):
#     def discounted_price(self, discount_percentage):
#         total = self.total_price()
#         discount = total * (discount_percentage / 100)
#         return total - discount




from turtle import Turtle, Screen
import random
import heroes

colors = ["red", "green", "blue", "yellow", "purple", "orange"]

t = Turtle()
t.shape("circle")
t.color(random.choice(colors))

#drawing a square

for _ in range(4):
    t.forward(100)
    t.right(90)


screen = Screen ()
screen.exitonclick()