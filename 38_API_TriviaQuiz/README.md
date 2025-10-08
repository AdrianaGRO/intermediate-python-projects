# 🧠 Trivia Quiz Game

A graphical trivia quiz application that fetches questions from the Open Trivia Database API and presents them in an interactive GUI.

## Features
- Fetches 10 random true/false questions from Open Trivia DB
- Beautiful Tkinter GUI interface
- Real-time score tracking
- Visual feedback for correct/incorrect answers
- Object-oriented design with separate classes

## Files
- `main.py` - Main application entry point
- `data.py` - Fetches questions from the API
- `question_model.py` - Question class definition
- `quiz_brain.py` - Quiz logic and game management
- `ui.py` - GUI interface using Tkinter
- `images/` - Contains UI images

## API Used
- Open Trivia Database API (https://opentdb.com/)

## How to Run
1. Run `python main.py`
2. Answer the true/false questions by clicking the buttons
3. See your final score at the end!

## Requirements
- requests
- tkinter (usually comes with Python)

## Architecture
The app follows OOP principles with separate classes for questions, quiz logic, and the user interface.