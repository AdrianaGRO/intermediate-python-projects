import justpy as jp
from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary
from documentation import Documentation

# Import api.py to register its route
import api

# Register routes
jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)
jp.Route(Documentation.path, Documentation.serve)

def start_server(port=8000):
    """Try to start the JustPy server on the specified port."""
    try:
        print(f"Starting API Dictionary server on http://127.0.0.1:{port}")
        print(f"Documentation available at: http://127.0.0.1:{port}/documentation")  
        print(f"API endpoint: http://127.0.0.1:{port}/api?w=word")
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