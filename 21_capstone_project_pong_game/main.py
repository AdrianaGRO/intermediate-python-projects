from turtle import Turtle, Screen
import time

from paddles import Paddle, PADDLE_LEFT_POSITION, PADDLE_RIGHT_POSITION
from ball import Ball
from scoreboard import ScoreBoard, SCORE_LEFT_POSITION,SCORE_RIGHT_POSITION, GameOverBoard
from middle_line import MiddleLine
from replay_button import ReplayButton


def setup_game():
    """Initialize game components"""
    global screen, middle_line, paddle_left, paddle_right, replay_button, ball, game_over, score_left, score_right
    
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("PONG")
    screen.tracer(0) #Stop the animation
    
    middle_line = MiddleLine()
    middle_line.draw_line()
    
    paddle_left = Paddle(PADDLE_LEFT_POSITION)
    paddle_right = Paddle(PADDLE_RIGHT_POSITION)
    
    replay_button = ReplayButton()  # Button starts hidden
    ball = Ball()
    game_over = GameOverBoard()
    
    score_left = ScoreBoard(SCORE_LEFT_POSITION)
    score_right = ScoreBoard(SCORE_RIGHT_POSITION)
    
    screen.listen()
    screen.onkey(paddle_right.up, "Up")
    screen.onkey(paddle_right.down, "Down")
    screen.onkey(paddle_left.up, "w")
    screen.onkey(paddle_left.down, "s")

def reset_game():
    """Reset the game to initial state"""
    global ball, score_left, score_right, game_over, replay_button
    
    # Clear game over message and hide replay button
    game_over.clear()
    replay_button.hide()
    
    # Reset ball
    ball.goto(0, 0)
    ball.move_speed = 0.2
    ball.reset_position()
    
    # Reset scores
    score_left.score = 0
    score_right.score = 0
    score_left.update_score()
    score_right.update_score()

def run_game():
    """Main game loop"""
    WINNING_SCORE = 5
    
    while True:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()
        
        # Detect collision with wall on x axis
        if ball.distance(paddle_left) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            ball.move_speed *= 0.9  # Increase speed 
        # Detect collision with wall on y axis
        if ball.distance(paddle_right) < 50 and ball.xcor() > 320:
            ball.bounce_x()
            ball.move_speed *= 0.9  # Increase speed 
        
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Right paddle misses
        if ball.xcor() > 380:
            score_left.increase_score()
            ball.goto(0, 0)
            ball.bounce_x()
            ball.move_speed = 0.2  # reset speed
            ball.reset_position()

            if score_left.score == WINNING_SCORE:
                game_over.display_winner("Left Player")
                replay_button.show()  # Show replay button
                return  # Exit game loop
        
        #Left paddle misses
        if ball.xcor() < -380:
            score_right.increase_score()
            ball.goto(0, 0)
            ball.bounce_x()
            ball.move_speed = 0.2  # reset speed
            ball.reset_position()
            
            if score_right.score == WINNING_SCORE:
                game_over.display_winner("Right Player")
                replay_button.show()  # Show replay button
                return  # Exit game loop

        score_left.update_score()
        score_right.update_score()

def on_click(x, y):
    """Handle screen clicks"""
    if replay_button.is_click_on_button(x, y):
        reset_game()
        run_game()  # Start a new game

# Initialize and start the game
setup_game()
screen.onscreenclick(on_click)
run_game()
screen.mainloop()
