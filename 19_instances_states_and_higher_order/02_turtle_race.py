# --- Imports ---
from turtle import Turtle, Screen
import random
import time

# --- Screen and Turtle Setup ---
screen = Screen()
screen.title("Turtle Racing 🐢")
screen.setup(width=600, height=600)
screen.bgcolor("#eff2ff")

t = Turtle()
t.hideturtle()

# --- Game Settings ---
num_turtles = int(screen.numinput("Number of Turtles", "How many turtles do you want to race, between 2 and 6?", minval=2, maxval=6))
turtle_colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [ -250, -150, -50, 50, 150, 250 ]

# --- Function to draw the finish line ---
def draw_finish_line():
    """Draws the vertical finish line on the screen."""
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(250, -280)
    finish_line.pendown()
    finish_line.pensize(3)
    finish_line.color("black")
    finish_line.goto(250, 280)

# --- Function to create the turtles ---
def setup_turtles(num_turtles, turtle_colors, y_positions):
    """Creates and returns a list of turtle racers."""
    turtles = []
    for i in range(num_turtles):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(turtle_colors[i])
        new_turtle.penup()
        new_turtle.goto(-250, y_positions[i])
        turtles.append(new_turtle)
    return turtles

# --- Function to reset turtles to starting positions ---
def reset_turtles(turtles, y_positions):
    """Resets all turtles to the starting line."""
    for i, turtle in enumerate(turtles):
        turtle.penup()
        turtle.goto(-250, y_positions[i])
        turtle.pendown()

# --- Function to get the user's bet ---
def get_user_bet(num_turtles, turtle_colors):
    """Prompts the user to bet on a turtle color."""
    prompt_colors = ", ".join(turtle_colors[:num_turtles])
    bet = screen.textinput(title = "Make your bet", prompt = f"Who will win the race? Enter a color ({prompt_colors}): ")
    valid_colors = turtle_colors[:num_turtles]
    while bet not in valid_colors:
        bet = screen.textinput(title = "Invalid color", prompt = f"Invalid color. Please choose from the following: {prompt_colors}: ")
    return bet

# --- Function to run the race ---
def run_the_race(turtles, user_bet):
    """Runs the turtle race and announces the winner."""
    while True:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() >= 250:
                winning_color = turtle.pencolor()
                screen.clear()
                # Create a new turtle for writing the message after clearing
                message_turtle = Turtle()
                message_turtle.hideturtle()
                message_turtle.penup()
                message_turtle.goto(0, 0)
                if winning_color == user_bet:
                    screen.bgcolor("#e7f9bf")
                    message_turtle.write(f"🏆 You've won! The {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "bold"))
                else:
                    screen.bgcolor("#fcc9c6")
                    message_turtle.write(f"😩 You've lost! The {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "bold"))
                return

# --- Main game loop ---
def main():
    """Main game loop for the turtle race."""
    while True:
        screen.clear()
        screen.bgcolor("#eff2ff")
        # Recreate turtles each time to avoid state issues
        turtles = setup_turtles(num_turtles, turtle_colors, y_positions)
        draw_finish_line()
        bet = get_user_bet(num_turtles, turtle_colors)
        run_the_race(turtles, bet)
        
        # Wait 2 seconds before asking to play again
        time.sleep(2)
        
        play_again = screen.textinput("Play Again?", "Do you want to play again? (yes/no): ")
        if not play_again or play_again.lower() != "yes":
            break
    screen.bye()

main()
# --- End of game ---