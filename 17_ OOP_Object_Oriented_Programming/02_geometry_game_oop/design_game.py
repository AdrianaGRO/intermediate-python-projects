import turtle


def draw_rectangle_turtle(rectangle, user_point, is_inside):
    t = turtle.Turtle()
    t.speed(1)
    t.penup()
    scale = 20

    # Draw axes
    t.goto(-10 * scale, 0)
    t.pendown()
    t.goto(20 * scale, 0)
    t.penup()
    t.goto(0, -10 * scale)
    t.pendown()
    t.goto(0, 20 * scale)

    # Draw tick marks and labels for x axis
    t.penup()
    for x in range(0, 21, 1):
        t.goto(x * scale, -5)
        t.pendown()
        t.goto(x * scale, 5)
        t.penup()
        t.goto(x * scale - 5, -20)
        t.write(str(x), align="center", font=("Arial", 8, "normal"))

    # Draw tick marks and labels for y axis
    for y in range(0, 21, 1):
        t.goto(-5, y * scale)
        t.pendown()
        t.goto(5, y * scale)
        t.penup()
        t.goto(-20, y * scale - 5)
        t.write(str(y), align="center", font=("Arial", 8, "normal"))

    # Draw rectangle
    t.penup()
    t.goto(rectangle.lower_left.x * scale, rectangle.lower_left.y * scale)
    t.pendown()
    t.goto(rectangle.upper_right.x * scale, rectangle.lower_left.y * scale)
    t.goto(rectangle.upper_right.x * scale, rectangle.upper_right.y * scale)
    t.goto(rectangle.lower_left.x * scale, rectangle.upper_right.y * scale)
    t.goto(rectangle.lower_left.x * scale, rectangle.lower_left.y * scale)

    # Draw user point
    t.penup()
    t.goto(user_point.x * scale, user_point.y * scale)
    if is_inside:
        t.dot(15, "green")
    else:
        t.dot(15, "red")
    t.hideturtle()
    turtle.done()
