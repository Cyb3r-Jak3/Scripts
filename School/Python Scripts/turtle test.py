from turtle import *
bot = Turtle()
canvas = Screen()
canvas.setup(500,500)
letter = raw_input("What letter would you like drawn? ").upper
if letter == "A":
    bot.left(75)
    bot.forward(100)
    bot.right(150)
    bot.forward(100)
    bot.back(50)
    bot.right(105)
    bot.forward(28)
    bot.ht()
if letter == "B":
    bot.left(90)
    bot.forward(200)
    bot.right(90)
    bot.forward(75)
    bot.right(90)
    bot.forward(80)
    bot.right(90)
    bot.forward(75)
    bot.left(90)
    bot.forward(10)
    bot.left(90)
    bot.forward(75)
    bot.right(90)
    bot.forward(110)
    bot.right(90)
    bot.forward(75)
    bot.ht()
if letter == 'C':
    bot.pu()
    bot.setpos(100, 100)
    bot.pd()
    bot.left(180)
    bot.forward(100)
    bot.left(90)
    bot.forward(100)
    bot.left(90)
    bot.forward(100)
    bot.ht()
    
