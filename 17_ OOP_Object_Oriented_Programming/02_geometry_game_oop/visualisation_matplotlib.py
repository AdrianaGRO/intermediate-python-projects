

# Visualization using matplotlib
import matplotlib.pyplot as plt

def draw_rectangle(lower_left, upper_right, color='blue', label='Rectangle'):
    x0, y0 = lower_left
    x1, y1 = upper_right
    width = x1 - x0
    height = y1 - y0
    rect = plt.Rectangle((x0, y0), width, height, fill=False, edgecolor=color, linewidth=2, label=label)
    plt.gca().add_patch(rect)

# Draw rectangle
draw_rectangle((3, 10), (14, 11), color='blue', label='Rect (3,10)-(14,11)')

# Draw point (3, 14)
plt.scatter([3], [14], color='red', s=100, zorder=5, label='Point (3,14)')
plt.text(3 + 0.1, 14, 'Point (3,14)', color='red')

# Set plot limits and properties
plt.xlim(-1, 20)
plt.ylim(-1, 20)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title('Point and Rectangle Visualization')
plt.grid(True)
plt.show()

