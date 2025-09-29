import justpy as jp
import definition
from .layout import Layout
import requests

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
               Get the definition of an english word using our RESTful API.
               """, a=div, classes="text-lg m-2 p-2")
        jp.Div(text="⚠️ Note: This requires the API server (folder 14) to be running on port 8000.", 
               a=div, classes="text-sm m-2 p-2 bg-yellow-100 border border-yellow-300 rounded")
        user_input = jp.Input(placeholder="Enter a word", a=div,
                              classes="m-2 p-2 py-2 px-4 border rounded bg-gray-100 border-gray-300 w-64 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent")
        
        output_div = jp.Div(a=div, classes="text-gray-700 m-2 p-2 text-lg border-2 h-40")
        
        # Create a function that gets definition when user types
        def get_definition_on_input(widget, msg):
            word = widget.value.strip().lower()
            if word:  # Only process if there's input
                try:
                    # Make API request to folder 14's REST API
                    response = requests.get(f"http://127.0.0.1:8000/api?w={word}")
                    
                    if response.status_code == 200:
                        data = response.json()
                        definitions = data.get("definition", [])
                        
                        if definitions and len(definitions) > 0:
                            if len(definitions) == 1:
                                output_div.text = f"Definition: {definitions[0]}"
                            else:
                                # Multiple definitions
                                result_text = "Definitions:\n"
                                for i, def_text in enumerate(definitions, 1):
                                    result_text += f"{i}. {def_text}\n"
                                output_div.text = result_text
                        else:
                            output_div.text = "No definition found."
                    else:
                        output_div.text = f"API Error: {response.status_code}"
                        
                except requests.exceptions.ConnectionError:
                    output_div.text = "Error: Cannot connect to API server. Make sure the API server (port 8000) is running."
                except requests.exceptions.RequestException as e:
                    output_div.text = f"Request Error: {str(e)}"
                except Exception as e:
                    output_div.text = f"Error: {str(e)}"
            else:
                output_div.text = ""  # Clear output if input is empty
            
        user_input.on('input', get_definition_on_input)

        return wp
