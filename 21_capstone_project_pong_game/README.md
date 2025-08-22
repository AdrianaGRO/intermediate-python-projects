# 🏓 Pong Game

A classic Pong game implementation using Python's Turtle graphics module. This is a two-player arcade game where players control paddles to hit a ball back and forth, trying to score points by getting the ball past their opponent's paddle.

## 🎮 Game Features

- **Two-player gameplay** with keyboard controls
- **Real-time scoring system** with visual scoreboard
- **Collision detection** for paddles and walls
- **Dynamic ball speed** that increases with each paddle hit
- **Game over screen** when a player reaches the winning score
- **Replay functionality** with a clickable restart button
- **Classic arcade aesthetics** with a centered middle line

## 🕹️ Controls

### Player 1 (Left Paddle)
- **w** - Move paddle up
- **s** - Move paddle down

### Player 2 (Right Paddle)
- **Up Arrow** - Move paddle up
- **Down Arrow** - Move paddle down

### Game Controls
- **Mouse Click** on Replay button - Restart the game after it ends

## 🎯 How to Play

1. **Objective**: Be the first player to score 5 points
2. **Scoring**: You score a point when the ball passes your opponent's paddle
3. **Ball Physics**: 
   - The ball bounces off the top and bottom walls
   - The ball speeds up slightly each time it hits a paddle
   - The ball resets to center after each point
4. **Winning**: First player to reach 5 points wins the game
5. **Replay**: Click the "Replay" button that appears after the game ends to start a new match

## 🚀 Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- Turtle graphics module (comes built-in with Python)

### Running the Game
1. Clone or download the project files
2. Navigate to the project directory:
   ```bash
   cd 21_capstone_project_pong_game
   ```
3. Run the main game file:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
21_capstone_project_pong_game/
├── main.py           # Main game loop and initialization
├── ball.py           # Ball class with movement and collision logic
├── paddles.py        # Paddle class with movement controls
├── scoreboard.py     # Scoring system and game over display
├── middle_line.py    # Visual middle line for the court
├── replay_button.py  # Restart button functionality
└── README.md         # 
```

## 🏗️ Code Architecture

### Main Components

#### `main.py`
- **Game initialization** and setup
- **Main game loop** with collision detection
- **Event handling** for keyboard and mouse inputs
- **Game state management** (setup, reset, restart)

#### `ball.py` - Ball Class
- Ball movement and physics
- Collision handling (bounce mechanics)
- Speed management
- Position reset functionality

#### `paddles.py` - Paddle Class
- Paddle creation and positioning
- Movement controls (up/down)
- Paddle collision boundaries

#### `scoreboard.py` - Scoring System
- Score tracking and display
- Game over message display
- Winner announcement

#### `middle_line.py` - Visual Elements
- Court middle line drawing
- Game aesthetics

#### `replay_button.py` - Replay Functionality
- Interactive restart button
- Click detection
- Game reset capabilities

## 🎨 Game Specifications

- **Screen Size**: 800x600 pixels
- **Background**: Black
- **Paddle Color**: White
- **Ball Color**: Purple
- **Paddle Size**: 5x1 units (stretched squares)
- **Ball Size**: 1x1 unit circle
- **Winning Score**: 5 points
- **Ball Speed**: Dynamic (increases with paddle hits)

## 🔧 Technical Features

### Object-Oriented Design
- Modular code structure with separate classes for each game component
- Inheritance from Turtle class for graphics objects
- Clean separation of concerns

### Game Mechanics
- **Collision Detection**: Ball-paddle and ball-wall collision detection
- **Physics Simulation**: Realistic ball bouncing with speed variation
- **State Management**: Proper game initialization, reset, and restart functionality
- **Event Handling**: Keyboard controls and mouse click detection

### Visual Features
- **Real-time Graphics**: Smooth animation using Turtle graphics
- **UI Elements**: Interactive replay button with proper styling
- **Game Feedback**: Clear winner announcement and scoring display

## 🎓 Learning Objectives

This project demonstrates:
- **Object-Oriented Programming** principles
- **Game development** fundamentals
- **Event-driven programming** with user inputs
- **Graphics programming** using Turtle
- **Collision detection** algorithms
- **State management** in interactive applications


### Common Issues
- **Game window doesn't appear**: Make sure you have Tkinter installed (usually comes with Python)
- **Controls not responding**: Click on the game window to ensure it has focus
- **Game runs too fast/slow**: The speed is controlled by the `time.sleep()` value in the main loop

