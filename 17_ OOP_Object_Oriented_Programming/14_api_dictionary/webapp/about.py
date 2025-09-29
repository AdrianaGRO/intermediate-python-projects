import justpy as jp
from .layout import Layout

class About:
    path = "/about"
    
    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage(tailwind=True)
        
        layout = Layout(a=wp)
        container = jp.QPageContainer(a=layout)
        page = jp.QPage(a=container, classes="bg-gray-50")
        
        div = jp.Div(text="About API Dictionary", a=page, classes="text-4xl font-bold text-center m-2 p-2")
        jp.Div(text="This is a RESTful API Dictionary built using JustPy and Python.", a=div, classes="text-lg text-center m-2 p-2")
        jp.Div(text="""
               API Dictionary allows users to look up definitions of English words via a simple REST API. 
               You can navigate to different sections using the menu on the left.
               Check out the Documentation section to learn how to use the API.
               """, a=div, classes="text-lg m-2 p-2")
        return wp
    


