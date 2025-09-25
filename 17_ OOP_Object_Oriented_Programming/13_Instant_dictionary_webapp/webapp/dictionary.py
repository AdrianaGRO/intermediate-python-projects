import justpy as jp
import definition
from .layout import Layout

class Dictionary:
    path = "/dictionary"
    
    @classmethod
    def serve(cls,request_object):
        wp = jp.QuasarPage(tailwind=True)
        
        layout = Layout(a=wp)
        container = jp.QPageContainer(a=layout)
        page = jp.QPage(a=container, classes="bg-gray-50")
        
        # Add dictionary content to the page, not container
        div = jp.Div(a=page, classes="text-4xl m-2 p-2")
        jp.Div(text="English Dictionary", a=div, classes="text-4xl m-2 p-2")
        jp.Div(text="""
               Get the definition of an english word.
               """, a=div, classes="text-lg m-2 p-2")
        user_input = jp.Input(placeholder="Enter a word", a=div,
                              classes="m-2 p-2 py-2 px-4 border rounded bg-gray-100 border-gray-300 w-64 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent")
        
        output_div = jp.Div(a=div, classes="text-gray-700 m-2 p-2 text-lg border-2 h-40")
        
        # Create a function that gets definition when user types
        def get_definition_on_input(widget, msg):
            if widget.value.strip():  # Only process if there's input
                defined = definition.Definition(widget.value)
                output_div.text = defined.get_definition()
            else:
                output_div.text = ""  # Clear output if input is empty
        
        user_input.on('input', get_definition_on_input)

        return wp
