import colorgram
import turtle as tom
import random
# color = colorgram.extract('/home/tamil/python_program/Day18/painting/image.jpg', 30)
# # print(color)
# rgb_colors = []

# for col in color:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color) 

# print(rgb_colors)

color_list = [(196, 165, 120), (139, 81, 59), (220, 201, 141), (63, 94, 119), (164, 151, 54), (139, 162, 178), (127, 35, 25), (70, 37, 31), 
 (53, 114, 87), (188, 98, 81), (148, 179, 153), (22, 90, 71), (160, 146, 157), (226, 177, 168), (33, 57, 72), 
 (111, 74, 77), (139, 21, 25), (182, 201, 177), (90, 144, 126), (12, 69, 61), (37, 76, 83), 
 (187, 89, 91), (37, 66, 93), (90, 25, 29), (108, 128, 151), (221, 179, 183)]

def dots(xaxis,yaxis):
    x = -280 ; y = -250
    tom.colormode(255)
    tom.hideturtle()
    tom.penup()
    tom.goto(x, y)
    tom.speed("fastest")

    for _ in range(yaxis):
        for _ in range(xaxis):
            tom.dot(20, random.choice(color_list))
            tom.penup()
            tom.fd(50)
        y = y+50
        tom.goto(x=x, y=y)
    tom.exitonclick()


dots(10,10)



"""
program requirements

TODO: 10/10 dot painting
TODO: dot size is 20
TODO: space between dots is 50
"""
"""
step1:print the dot 10/10 ✅
step2:change the postion of the starting ✅
step3:set the random colors for dots ✅
step4:need to print 100 dots in 10/10 ✅
""" 
