"""
Better coordinate detector with visible feedback for Spain
"""

from turtle import Turtle, Screen
import os

class CoordinateDetector:
    def __init__(self):
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.screen = Screen()
        self.screen.title("Spain Map - Click for Coordinates")
        self.screen.setup(width=800, height=800)
        
        # Load the map with absolute path
        image_path = os.path.join(script_dir, "pan.gif")
        self.screen.addshape(image_path)
        
        # Create map turtle
        self.map_turtle = Turtle()
        self.map_turtle.penup()
        self.map_turtle.shape(image_path)
        self.map_turtle.goto(0, 0)
        
        # Create text display turtle
        self.text_turtle = Turtle()
        self.text_turtle.hideturtle()
        self.text_turtle.penup()
        self.text_turtle.color("red")
        self.text_turtle.goto(-380, 350)
        
        # Create marker turtle to show where you clicked
        self.marker = Turtle()
        self.marker.shape("circle")
        self.marker.color("red")
        self.marker.penup()
        self.marker.hideturtle()
        
        self.coordinates = []
        self.show_instructions()
        
        # Set up click detection
        self.screen.onclick(self.get_coordinates)
        self.screen.listen()
        
    def show_instructions(self):
        """Show instructions on screen"""
        self.text_turtle.write("Click on any Spanish province\nCoordinates will show here\nPress ESC to exit", 
                              font=("Arial", 12, "bold"))
    
    def get_coordinates(self, x, y):
        """Get and display coordinates"""
        # Clear previous text
        self.text_turtle.clear()
        
        # Show coordinates
        coord_text = f"x={int(x)}, y={int(y)}\n\nClick anywhere else\nPress ESC to exit"
        self.text_turtle.write(coord_text, font=("Arial", 12, "bold"))
        
        # Show marker at clicked location
        self.marker.goto(x, y)
        self.marker.showturtle()
        
        # Print to terminal too
        print(f"Clicked at: x={int(x)}, y={int(y)}")
        
        # Store coordinates
        self.coordinates.append((int(x), int(y)))
    
    def run(self):
        """Keep the screen open"""
        print("Click on the Spanish provinces to get coordinates.")
        print("The coordinates will appear both on screen and in the terminal.")
        print("Use these coordinates to fix LUGO and Asturias positions.")
        print("Press ESC or close the window when done.")
        
        # Keep the screen open until user presses a key or closes window
        self.screen.listen()
        self.screen.onkey(self.screen.bye, "Escape")
        self.screen.mainloop()

if __name__ == "__main__":
    detector = CoordinateDetector()
    detector.run()
