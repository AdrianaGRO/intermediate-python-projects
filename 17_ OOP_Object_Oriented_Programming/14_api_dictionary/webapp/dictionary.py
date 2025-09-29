import justpy as jp
import definition
from .layout import Layout

class Dictionary:
    path = "/dictionary"
    
    @classmethod
    def serve(cls, request_object):
        wp = jp.QuasarPage(tailwind=True)
        
        layout = Layout(a=wp)
        container = jp.QPageContainer(a=layout)
        page = jp.QPage(a=container, classes="bg-gray-50")
        
        # Title section
        title_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        jp.H1(text="English Dictionary", a=title_div, classes="text-4xl font-bold text-blue-600 mb-4")
        jp.P(text="Enter a word below to get its definition:", a=title_div, classes="text-lg text-gray-700 mb-4")
        
        # Search section
        search_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        
        user_input = jp.Input(
            placeholder="Enter a word...", 
            a=search_div,
            classes="w-full p-3 border border-gray-300 rounded-lg text-lg mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
        )
        
        search_button = jp.Button(
            text="Search", 
            a=search_div,
            classes="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg text-lg mr-4"
        )
        
        clear_button = jp.Button(
            text="Clear", 
            a=search_div,
            classes="bg-gray-500 hover:bg-gray-700 text-white font-bold py-3 px-6 rounded-lg text-lg"
        )
        
        # Results section
        results_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        output_div = jp.Div(a=results_div, classes="text-gray-700 text-lg leading-relaxed min-h-[100px]")
        output_div.text = "Enter a word above and click Search to see its definition."
        
        def search_word(widget, msg):
            word = user_input.value.strip().lower()
            
            if not word:
                output_div.text = "Please enter a word to search."
                output_div.classes = "text-red-600 text-lg leading-relaxed min-h-[100px]"
                return
            
            try:
                # Get definition using the correct method name
                definition_obj = definition.Definition(word)
                definitions = definition_obj.get()  # This is the correct method name
                
                if definitions and len(definitions) > 0:
                    output_div.classes = "text-gray-700 text-lg leading-relaxed min-h-[100px]"
                    
                    if len(definitions) == 1:
                        output_div.text = f"Definition of '{word}':\n\n{definitions[0]}"
                    else:
                        result_text = f"Definitions of '{word}':\n\n"
                        for i, def_text in enumerate(definitions, 1):
                            result_text += f"{i}. {def_text}\n\n"
                        output_div.text = result_text
                else:
                    output_div.text = f"Sorry, no definition found for '{word}'. Please try another word."
                    output_div.classes = "text-yellow-600 text-lg leading-relaxed min-h-[100px]"
                    
            except Exception as e:
                output_div.text = f"An error occurred while searching: {str(e)}"
                output_div.classes = "text-red-600 text-lg leading-relaxed min-h-[100px]"
        
        def clear_search(widget, msg):
            user_input.value = ""
            output_div.text = "Enter a word above and click Search to see its definition."
            output_div.classes = "text-gray-700 text-lg leading-relaxed min-h-[100px]"
        
        def handle_keydown(widget, msg):
            if msg['key'] == 'Enter':
                search_word(widget, msg)
        
        # Attach event handlers
        search_button.on('click', search_word)
        clear_button.on('click', clear_search)
        user_input.on('keydown', handle_keydown)
        
        # API info section
        api_info_div = jp.Div(a=page, classes="bg-blue-50 border-l-4 border-blue-400 shadow-lg rounded-lg m-4 p-6")
        jp.H3(text="💡 Developer Tip", a=api_info_div, classes="text-xl font-semibold text-blue-600 mb-3")
        jp.P(text="You can also access this dictionary programmatically via our API:", a=api_info_div, classes="text-blue-700 mb-2")
        jp.Code(text="GET /api?w=word", a=api_info_div, classes="bg-blue-100 px-2 py-1 rounded text-blue-800 font-mono")
        jp.Br(a=api_info_div)
        jp.A(text="📚 View API Documentation", href="/documentation", a=api_info_div, classes="text-blue-600 hover:text-blue-800 underline mt-2 inline-block")

        return wp
