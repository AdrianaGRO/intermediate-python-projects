from canvas import Canvas
from draw_geometrical_figures import Rectangle, Square

# Get canvas width, height and background color
canvas_width = int(input('Enter canvas width(e.g: 800): '))
canvas_height = int(input('Enter canvas height(e.g: 600): '))
try:
    color_input = input('Enter canvas background color (R G B) from (0-255): ')
    # Handle both space-separated and comma-separated inputs
    if ',' in color_input:
        canvas_color = list(map(int, color_input.split(',')))
    else:
        canvas_color = list(map(int, color_input.split()))
    # Ensure we have exactly 3 RGB values
    if len(canvas_color) != 3:
        print("Error: Please provide 3 values for RGB. Using default white color.")
        canvas_color = [255, 255, 255]
except ValueError:
    print("Error parsing color values. Using default white color.")
    canvas_color = [255, 255, 255]

# Create a canvas object
canvas = Canvas(width=canvas_width, height=canvas_height, color=canvas_color)

while True:
    shape = input('Enter shape to draw (rectangle/square) or "q" to quit: ').lower()
    if shape == 'q':
        break
    elif shape == 'rectangle':
        x = int(input('Enter x position: '))
        y = int(input('Enter y position: '))
        width = int(input('Enter rectangle width(eg: 10): '))
        height = int(input('Enter rectangle height(eg: 5): '))
        try:
            color_input = input('Enter rectangle color (R G B): ')
            # Handle both space-separated and comma-separated inputs
            if ',' in color_input:
                color = list(map(int, color_input.split(',')))
            else:
                color = list(map(int, color_input.split()))
            # Ensure we have exactly 3 RGB values
            if len(color) != 3:
                print("Error: Please provide 3 values for RGB. Using default blue color.")
                color = [0, 0, 255]
        except ValueError:
            print("Error parsing color values. Using default blue color.")
            color = [0, 0, 255]
        rect = Rectangle(x, y, width, height, color)
        rect.draw(canvas)
    elif shape == 'square':
        x = int(input('Enter x position(eg: 5): '))
        y = int(input('Enter y position(eg: 5): '))
        side = int(input('Enter square side length(eg: 10): '))
        try:
            color_input = input('Enter square color (R G B): ')
            # Handle both space-separated and comma-separated inputs
            if ',' in color_input:
                color = list(map(int, color_input.split(',')))
            else:
                color = list(map(int, color_input.split()))
            # Ensure we have exactly 3 RGB values
            if len(color) != 3:
                print("Error: Please provide 3 values for RGB. Using default red color.")
                color = [255, 0, 0]
        except ValueError:
            print("Error parsing color values. Using default red color.")
            color = [255, 0, 0]
        square = Square(x, y, side, color)
        square.draw(canvas)
    else:
        print("Invalid shape. Choose 'rectangle', 'square' or 'q'.")

# Debugging info
print(f"Canvas dimensions: {canvas.width}x{canvas.height}")
print(f"Canvas shape: {canvas.data.shape}")
print(f"Canvas content summary: min={canvas.data.min()}, max={canvas.data.max()}")

# Save the canvas to an image file
canvas.make_pixel('canvas.png')
print("Canvas saved as 'canvas.png'")