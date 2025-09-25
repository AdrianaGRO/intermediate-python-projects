import justpy as jp
from .layout import Layout

class About:
    path = "/about"
    
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        
        layout = Layout(a=wp)
        container = jp.QPageContainer(a=layout)
        page = jp.QPage(a=container, classes="bg-gray-50")
        
        div = jp.Div(text="About Dictionary", a=page, classes="text-4xl m-2 p-2")
        jp.Div(text="This is a simple web application built using JustPy and Python.", a=div, classes="text-lg m-2 p-2")
        jp.Div(text="""
               Dictionary App allows users to look up definitions of English words. 
               You can navigate to different sections using the menu on the left.
               """, a=div, classes="text-lg m-2 p-2")
        return wp
    


