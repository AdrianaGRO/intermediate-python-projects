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
        
        # Welcome section
        welcome_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        jp.H1(text="Welcome to API Dictionary", a=welcome_div, classes="text-4xl font-bold text-blue-600 text-center mb-4")
        jp.P(text="A comprehensive dictionary application with both web interface and API access.", a=welcome_div, classes="text-lg text-gray-700 text-center mb-6")
        
        # Features section
        features_div = jp.Div(a=page, classes="bg-white shadow-lg rounded-lg m-4 p-6")
        jp.H2(text="Features", a=features_div, classes="text-2xl font-semibold text-blue-600 mb-4")
        
        # Feature cards
        cards_container = jp.Div(a=features_div, classes="grid md:grid-cols-2 gap-6")
        
        # Dictionary card
        dict_card = jp.Div(a=cards_container, classes="bg-blue-50 border border-blue-200 rounded-lg p-4")
        jp.H3(text="📚 Interactive Dictionary", a=dict_card, classes="text-xl font-semibold text-blue-700 mb-2")
        jp.P(text="Look up word definitions using our user-friendly web interface. Perfect for quick searches and learning.", a=dict_card, classes="text-gray-700 mb-3")
        jp.A(text="Try Dictionary →", href="/dictionary", a=dict_card, classes="text-blue-600 hover:text-blue-800 underline font-medium")
        
        # API card
        api_card = jp.Div(a=cards_container, classes="bg-green-50 border border-green-200 rounded-lg p-4")
        jp.H3(text="🔌 REST API", a=api_card, classes="text-xl font-semibold text-green-700 mb-2")
        jp.P(text="Access dictionary data programmatically via our RESTful API. Perfect for developers and applications.", a=api_card, classes="text-gray-700 mb-3")
        jp.A(text="View API Docs →", href="/documentation", a=api_card, classes="text-green-600 hover:text-green-800 underline font-medium")
        
        # Quick start section
        quickstart_div = jp.Div(a=page, classes="bg-gradient-to-r from-blue-50 to-green-50 border-l-4 border-blue-400 shadow-lg rounded-lg m-4 p-6")
        jp.H2(text="🚀 Quick Start", a=quickstart_div, classes="text-2xl font-semibold text-blue-600 mb-4")
        
        quick_list = jp.Ul(a=quickstart_div, classes="list-disc list-inside space-y-2 text-gray-700")
        jp.Li(text="🔍 Use the Dictionary to search for word definitions interactively", a=quick_list)
        jp.Li(text="📖 Check the API Documentation to learn about programmatic access", a=quick_list) 
        jp.Li(text="🧪 Test the API directly: /api?w=word", a=quick_list)
        jp.Li(text="ℹ️ Learn more in the About section", a=quick_list)
        
        return wp