# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('images.jpg.jpeg',35)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle

color_list = [(59, 105, 147), (224, 202, 112), (217, 146, 79), (143, 176, 199), (126, 88, 62), (196, 146, 171),
              (142, 77, 101), (215, 92, 65), (190, 82, 113), (138, 181, 141), (67, 110, 93), (148, 133, 69),
              (61, 157, 101), (44, 156, 187), (183, 191, 204), (113, 122, 149), (218, 176, 191), (16, 56, 93),
              (17, 68, 118), (175, 202, 182), (237, 172, 159), (158, 205, 217), (122, 41, 52), (163, 30, 25),
              (70, 57, 44), (219, 202, 33), (44, 61, 59), (75, 65, 49), (52, 72, 70)]

from turtle import Turtle, Screen
import random

pen1 = Turtle()
screen = Screen()
rcolor = random.choice(color_list)

def draw_hist():

    for dot in range(10):
        rcolor = random.choice(color_list)
        pen1.color(rcolor)
        pen1.dot(size=20)
        pen1.up()
        pen1.forward(50)


pen1.hideturtle()
pen1.speed('fastest')
turtle.colormode(255)
pos = float(-100.00)
pen1.up()
pen1.setpos(0.00, -150.00)
pen1.down()
for row in range(10):
    draw_hist()
    pen1.setpos(00, pos)
    pos += 50.00

screen.exitonclick()