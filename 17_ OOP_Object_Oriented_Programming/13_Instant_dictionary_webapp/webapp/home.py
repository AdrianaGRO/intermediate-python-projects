import justpy as jp
from .layout import Layout

class Home:
    path = "/"
    
    @classmethod
    def serve(cls, request):
        
        wp = jp.QuasarPage(tailwind=True)
        layout = Layout(a=wp)
        container = jp.QPageContainer(a=layout)
        
        page = jp.QPage(a=container, classes="bg-gray-50")
        div = jp.Div(text="Home Page", a=page, classes="text-4xl font-bold text-center m-2 p-2")
        jp.Div(text="This is a simple web application built using JustPy and Python.", a=div, classes="text-lg text-center m-2 p-2")
        jp.Div(text="""
               It demonstrates the use of JustPy for building interactive web applications. 
               This app includes a dictionary feature that allows users to look up definitions of English words. 
               You can navigate to different sections using the menu on the left.
              Enjoy using the Instant Dictionary!           """, a=div, classes="text-lg m-2 p-2")
        
        return wp