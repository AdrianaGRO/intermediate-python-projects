"""
Visualize current province coordinates as X marks on the Spain map
"""
import os
import pandas as pd
from turtle import Turtle, Screen

def load_provinces():
    """Load provinces from CSV file"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "provinces_correct.csv")
    
    try:
        df = pd.read_csv(csv_path)
        return [(row.province, row.x, row.y) for _, row in df.iterrows()]
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []

def visualize_coordinates():
    """Visualize all current coordinates on the map"""
    provinces = load_provinces()
    
    if not provinces:
        print("No provinces loaded!")
        return
    
    print(f"Total provinces loaded: {len(provinces)}")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "pan.gif")
    
    screen = Screen()
    screen.title("Spain Current Province Coordinates Visualizer")
    screen.setup(width=800, height=800)
    screen.addshape(image_path)
    
    # Create map turtle
    map_turtle = Turtle()
    map_turtle.penup()
    map_turtle.shape(image_path)
    map_turtle.goto(0, 0)
    
    # Draw X at each coordinate
    for province, x, y in provinces:
        marker = Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(x, y)
        marker.pendown()
        marker.pensize(2)
        
        # Highlight provinces being investigated/confirmed with new coordinates
        confirmed_provinces = [
            "A Coruna", "Albacete", "Alicante", "Almeria", "Asturias", "Avila", "Badajoz", "Barcelona", "Burgos", "Caceres", "Cadiz", "Cantabria", "Castellon", "Ciudad Real", "Cordoba", "Cuenca", "Gerona", "Granada", "Guadalajara", "Huelva", "Huesca", "Jaen", "Leon", "Lerida", "La Rioja", "Lugo", "Madrid", "Malaga", "Murcia", "Navarra", "Orense", "Palencia", "Pontevedra", "Salamanca", "Segovia", "Sevilla", "Soria", "Tarragona", "Teruel", "Toledo", "Valencia", "Valladolid", "Vizcaya", "Guipuzcoa", "Alava", "Zamora", "Zaragoza", "Ceuta", "Melilla", "Menorca", "Mallorca", "Ibiza", "Lanzarote", "Fuerteventura", "Gran Canaria", "Tenerife", "La Gomera", "La Palma", "El Hierro"
        ]
        if province in confirmed_provinces:
            marker.color("green")  # Green for confirmed coordinates
            print(f"CONFIRMED PROVINCE: {province} at ({x}, {y})")
        else:
            marker.color("blue")   # Blue for original coordinates
        
        # Draw X
        marker.setheading(45)
        marker.forward(8)
        marker.backward(16)
        marker.forward(8)
        marker.setheading(-45)
        marker.forward(8)
        marker.backward(16)
        marker.forward(8)
        marker.penup()
        
        # Show province name
        marker.goto(x, y-12)
        marker.write(province, align="center", font=("Arial", 10, "bold"))
    
    print("Green X marks show provinces with confirmed coordinates")
    print("Blue X marks show provinces still using original coordinates")
    print("Check the map to see which provinces are missing or misplaced!")
    
    screen.mainloop()

if __name__ == "__main__":
    visualize_coordinates()
