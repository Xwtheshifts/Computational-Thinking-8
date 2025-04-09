import turtle

t = turtle.Turtle()
# Color
t.color("white")
turtle.Screen().bgcolor("black")

# Color Changing Shape
colors = ["pink", "gray", "gold"]
for i in range(10000):
        t.color(colors[i % 3])
        t.forward(100)
        t.left(600 + 1)
# Speed
        t.speed(10000000000000000000000000000000000000000000000000000000000000)

turtle.exitonclick()