from turtle import Turtle, Screen
from turtle_player import Player
import time
from car_management import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

def play_again():
    global game_is_on, player, car_manager, scoreboard
    
    # Turn off animation and clean up all objects
    screen.tracer(0)
    
    # Clean up player
    player.penup()
    player.hideturtle()
    
    # Clean up scoreboard
    scoreboard.penup()
    scoreboard.hideturtle()
    
    # Clean up all cars
    for car in car_manager.cars:
        car.penup()
        car.hideturtle()
    
    # Clear the screen completely
    screen.clear()
    screen.bgcolor("white")  # Reset background
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing")
    screen.tracer(0)
    
    # Recreate game objects
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    
    # Reset key bindings
    screen.listen()
    screen.onkey(key="Up", fun=player.move_up)
    
    game_is_on = True
    game_loop()

def reset_game():
    global player, car_manager, scoreboard
    player.reset_position()
    car_manager.reset_cars()
    scoreboard.reset_score()

def exit_game():
    global game_is_on
    game_is_on = False
    screen.bye()

def game_loop():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        car_manager.create_car()
        car_manager.move_cars()

        # Detect collisions
        for car in car_manager.cars:
            if car.distance(player) < 20:
                    game_is_on = False
                    scoreboard.game_over()
                    time.sleep(1)
                    ask_play_again()
                    return

        if player.ycor() > 280:
            player.reset_position()
            car_manager.level_up()
            scoreboard.increase_score()


def ask_play_again():
    scoreboard.play_again_prompt()
    screen.onkey(fun=play_again, key="y")
    screen.onkey(fun=play_again, key="Y")
    screen.onkey(fun=exit_game, key="n")
    screen.onkey(fun=exit_game, key="N")
    screen.listen()


game_is_on = True

game_loop()

screen.exitonclick()