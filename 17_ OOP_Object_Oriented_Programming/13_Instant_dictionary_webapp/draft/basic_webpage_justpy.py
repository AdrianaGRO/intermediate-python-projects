import justpy as jp


@jp.SetRoute("/")
@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes= "bg-purple-200 h-screen")
    
    div1 = jp.Div(a=div, classes= "grid grid-cols-3 gap-4 m-2 p-2 p-4")
    input_number1 = jp.Input(a=div1, placeholder="Type a number...", classes="text-gray-700 m-2 p-2 ")
    input_number2 = jp.Input(a=div1, placeholder="Type a number...", classes="text-gray-700 m-2 p-2 ")
    d_output = jp.Div(text="Results will be displayed here.", a=div1, classes="text-gray-700 m-2 p-2 ")
    jp.Div(text="Learn more.", a=div1, classes="m-2 p-2 ")

    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4 m-2 p-2")
    jp.Button(text="Calculate", a=div2, click = sum_up, input_number1=input_number1, input_number2=input_number2,
              d = d_output,
              classes="m-2 py-1 px-4 bg-blue-500 text-white rounded hover:bg-red-700 hover:text-white transition-colors duration-200")

    jp.Div(text="Python and JustPy.", a=div2, mouseenter=mouse_enter,mouseleave=mouse_leave,
           classes="m-2 p-2 text-white rounded hover:bg-red-700 hover:text-white transition-colors duration-200")

    return wp

def sum_up(widget, msg):
    sum = float(widget.input_number1.value) + float(widget.input_number2.value)
    widget.d.text = f"The sum is: {sum}"
    
    
def mouse_enter(widget, msg):
    widget.text = "Hours and hours of practice will make you a master!"
    widget.classes = "m-2 p-2 bg-blue-500 text-white rounded hover:bg-red-700 hover:text-white transition-colors duration-200"
    widget.update()

def mouse_leave(widget, msg):
    widget.text = "Python and JustPy."
    widget.classes = "m-2 p-2 text-white rounded hover:bg-red-700 hover:text-white transition-colors duration-200"
    widget.update()













def start_server(port=8000):
    """Try to start the JustPy server on the specified port."""
    try:
        print(f"Attempting to start JustPy server on http://127.0.0.1:{port}")
        jp.justpy(host="127.0.0.1", port=port)
        return True
    except OSError as e:
        if "Address already in use" in str(e) or "errno 48" in str(e).lower():
            print(f"Port {port} is already in use.")
            return False
        else:
            print(f"Error starting server on port {port}: {e}")
            return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    # Try ports 8000, 8001, 8002, 8003
    ports_to_try = [8000, 8001, 8002, 8003]
    server_started = False
    
    for port in ports_to_try:
        if start_server(port):
            server_started = True
            break
    
    if not server_started:
        print("Could not start server on any of the attempted ports.")
        print("Please check that no other servers are running or manually specify a different port.")