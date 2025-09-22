from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
import wikipedia
import os


Builder.load_file('frontend.kv')

os.makedirs("files", exist_ok=True)


class FirstScreen(Screen):
    def search_image(self):
        query = self.get_user_query()
        image_path = "files/image.jpg"
        try:
            image_url = self.get_wikipedia_image_url(query)
            if image_url:
                self.download_image(image_url, image_path)
                self.update_image_ui(image_path)
            else:
                print("No images found on the Wikipedia page.")
        except wikipedia.exceptions.PageError:
            print(f"Could not find a page for '{query}'. Please try another query.")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_user_query(self):
        return self.manager.current_screen.ids.user_query.text.strip()

    def get_wikipedia_image_url(self, query):
        page = wikipedia.page(query, auto_suggest=False)
        if page.images:
            return page.images[0]
        return None

    def download_image(self, url, path):
        headers = {'User-Agent': 'MyKivyApp/1.0 (https://example.com)'}
        req = requests.get(url, headers=headers)
        with open(path, "wb") as f:
            f.write(req.content)

    def update_image_ui(self, image_path):
        self.manager.current_screen.ids.img.source = image_path
        self.manager.current_screen.ids.img.reload()


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    
    def build(self):
        return RootWidget()
    
    
MainApp().run()

