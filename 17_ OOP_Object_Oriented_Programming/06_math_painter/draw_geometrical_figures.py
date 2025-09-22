class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        print(f"Drawing rectangle at ({self.x}, {self.y}) with size {self.width}x{self.height} and color {self.color}")
        try:
            # Ensure coordinates are within canvas boundaries
            x_start = max(0, self.x)
            y_start = max(0, self.y)
            x_end = min(canvas.width, self.x + self.width)
            y_end = min(canvas.height, self.y + self.height)
            
            if x_start >= x_end or y_start >= y_end:
                print("Warning: Rectangle is outside canvas bounds!")
                return
                
            canvas.data[y_start:y_end, x_start:x_end] = self.color
            print(f"Rectangle drawn successfully from ({x_start}, {y_start}) to ({x_end}, {y_end})")
        except Exception as e:
            print(f"Error drawing rectangle: {e}")

class Square:
    def __init__(self, x,y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
        
    def draw(self, canvas):
        print(f"Drawing square at ({self.x}, {self.y}) with side {self.side} and color {self.color}")
        try:
            # Ensure coordinates are within canvas boundaries
            x_start = max(0, self.x)
            y_start = max(0, self.y)
            x_end = min(canvas.width, self.x + self.side)
            y_end = min(canvas.height, self.y + self.side)
            
            if x_start >= x_end or y_start >= y_end:
                print("Warning: Square is outside canvas bounds!")
                return
                
            canvas.data[y_start:y_end, x_start:x_end] = self.color
            print(f"Square drawn successfully from ({x_start}, {y_start}) to ({x_end}, {y_end})")
        except Exception as e:
            print(f"Error drawing square: {e}")

