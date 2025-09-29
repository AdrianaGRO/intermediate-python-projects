import justpy as jp
from webapp.layout import Layout

class Documentation:
    path = "/documentation"
    
    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage(tailwind=True)
        
        layout = Layout(a=wp)
        container = jp.QPageContainer(a=layout)
        page = jp.QPage(a=container, classes="bg-gray-50")
        
        # Main title
        title_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        jp.H1(text="API Dictionary Documentation", a=title_div, classes="text-4xl font-bold text-blue-600 mb-4")
        jp.P(text="Get definitions of English words via a simple RESTful API.", a=title_div, classes="text-lg text-gray-700 mb-4")
        
        # API Endpoint Section
        endpoint_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        jp.H2(text="API Endpoint", a=endpoint_div, classes="text-2xl font-semibold text-blue-600 mb-4")
        
        # Base URL
        jp.H3(text="Base URL:", a=endpoint_div, classes="text-lg font-medium text-gray-800 mb-2")
        jp.Div(text="http://127.0.0.1:8000", a=endpoint_div, classes="bg-gray-100 p-3 rounded font-mono text-lg mb-4")
        
        # API Format
        jp.H3(text="Request Format:", a=endpoint_div, classes="text-lg font-medium text-gray-800 mb-2")
        jp.Div(text="GET /api?w={word}", a=endpoint_div, classes="bg-gray-100 p-3 rounded font-mono text-lg mb-4")
        
        # Parameters
        params_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        jp.H2(text="Parameters", a=params_div, classes="text-2xl font-semibold text-blue-600 mb-4")
        
        # Parameter table
        table = jp.Table(a=params_div, classes="w-full border-collapse border border-gray-300")
        header = jp.Thead(a=table, classes="bg-gray-50")
        header_row = jp.Tr(a=header)
        jp.Th(text="Parameter", a=header_row, classes="border border-gray-300 px-4 py-2 text-left font-semibold")
        jp.Th(text="Type", a=header_row, classes="border border-gray-300 px-4 py-2 text-left font-semibold")
        jp.Th(text="Required", a=header_row, classes="border border-gray-300 px-4 py-2 text-left font-semibold")
        jp.Th(text="Description", a=header_row, classes="border border-gray-300 px-4 py-2 text-left font-semibold")
        
        tbody = jp.Tbody(a=table)
        row = jp.Tr(a=tbody)
        jp.Td(text="w", a=row, classes="border border-gray-300 px-4 py-2 font-mono")
        jp.Td(text="string", a=row, classes="border border-gray-300 px-4 py-2")
        jp.Td(text="Yes", a=row, classes="border border-gray-300 px-4 py-2 text-green-600 font-semibold")
        jp.Td(text="The word to look up in the dictionary", a=row, classes="border border-gray-300 px-4 py-2")
        
        # Examples Section
        examples_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        jp.H2(text="Examples", a=examples_div, classes="text-2xl font-semibold text-blue-600 mb-4")
        
        # Example 1
        jp.H3(text="Example 1: Look up 'sun'", a=examples_div, classes="text-lg font-medium text-gray-800 mb-2")
        jp.P(text="Request:", a=examples_div, classes="font-medium text-gray-700 mb-1")
        jp.Div(text="GET http://127.0.0.1:8000/api?w=sun", a=examples_div, classes="bg-gray-100 p-3 rounded font-mono mb-2")
        
        jp.P(text="Response:", a=examples_div, classes="font-medium text-gray-700 mb-1")
        response_json = '''{
    "word": "sun",
    "definition": [
        "The star that is the central body of the solar system...",
        "Light or warmth received from the sun's rays..."
    ]
}'''
        jp.Div(text=response_json, a=examples_div, classes="bg-gray-100 p-3 rounded font-mono text-sm mb-4 whitespace-pre")
        
        # Response Format Section
        response_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        jp.H2(text="Response Format", a=response_div, classes="text-2xl font-semibold text-blue-600 mb-4")
        jp.P(text="The API returns a JSON object with the following structure:", a=response_div, classes="text-gray-700 mb-3")
        
        # Response fields table
        resp_table = jp.Table(a=response_div, classes="w-full border-collapse border border-gray-300")
        resp_header = jp.Thead(a=resp_table, classes="bg-gray-50")
        resp_header_row = jp.Tr(a=resp_header)
        jp.Th(text="Field", a=resp_header_row, classes="border border-gray-300 px-4 py-2 text-left font-semibold")
        jp.Th(text="Type", a=resp_header_row, classes="border border-gray-300 px-4 py-2 text-left font-semibold")
        jp.Th(text="Description", a=resp_header_row, classes="border border-gray-300 px-4 py-2 text-left font-semibold")
        
        resp_tbody = jp.Tbody(a=resp_table)
        
        word_row = jp.Tr(a=resp_tbody)
        jp.Td(text="word", a=word_row, classes="border border-gray-300 px-4 py-2 font-mono")
        jp.Td(text="string", a=word_row, classes="border border-gray-300 px-4 py-2")
        jp.Td(text="The word that was looked up", a=word_row, classes="border border-gray-300 px-4 py-2")
        
        def_row = jp.Tr(a=resp_tbody)
        jp.Td(text="definition", a=def_row, classes="border border-gray-300 px-4 py-2 font-mono")
        jp.Td(text="array", a=def_row, classes="border border-gray-300 px-4 py-2")
        jp.Td(text="Array of definition strings for the word", a=def_row, classes="border border-gray-300 px-4 py-2")
        
        # Quick Test Section  
        test_div = jp.Div(a=page, classes="bg-blue-50 border-l-4 border-blue-400 shadow-lg rounded-lg m-4 p-6")
        jp.H2(text="Quick Test", a=test_div, classes="text-2xl font-semibold text-blue-600 mb-4")
        jp.P(text="Click the link below to test the API with the word 'sun':", a=test_div, classes="text-gray-700 mb-3")
        jp.A(text="http://127.0.0.1:8000/api?w=sun", href="/api?w=sun", target="_blank", 
             a=test_div, classes="text-blue-600 hover:text-blue-800 underline font-mono text-lg")
        
        return wp
    

