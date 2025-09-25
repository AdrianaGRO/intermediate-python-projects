import justpy as jp
from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary

# Automatically register routes for all classes with path and serve attributes
globals_copy = dict(globals())  # Create a copy to avoid iteration issues
for name, obj in globals_copy.items():
    # Check if it's a class (not a module or built-in) and has required attributes
    if (hasattr(obj, '__module__') and 
        hasattr(obj, 'path') and 
        hasattr(obj, 'serve') and
        not name.startswith('_')):  # Exclude built-ins
        jp.Route(obj.path, obj.serve)
        print(f"Registered route: {obj.path} -> {name}")
    


# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)    


jp.justpy(port=8001)

