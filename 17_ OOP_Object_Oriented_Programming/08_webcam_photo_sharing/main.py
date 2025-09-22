"""Title:  webcam photo sharer
Description: An app that starts the computer webcam, lets the user capture a photo and uploads the photo to the web and create a sharable link

Objects:
    Webcam:
        start()
        stop()
        capture()

    FileSharer:
        filepath()
        api
        share()
        """
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer
from kivy.core.clipboard import Clipboard
import pyperclip
import time

import time
Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    
    def start_stop(self):
        """Starts and stops the webcam and captures the photo"""
        self.ids.camera.opacity = 1
        if self.ids.camera.play:
            self.ids.camera.play = False
            self.ids.camera_button.text = "Start Camera"
            
        else:
            self.ids.camera.play = True
            self.ids.camera_button.text = "Stop Camera"
            

    def capture_photo(self):
        """Captures the photo from the webcam and switches to the image screen"""
        path = "/Users/adricati/Personal Development/intermediate-python-projects/17_ OOP_Object_Oriented_Programming/08_webcam_photo_sharing/files/"
        filename = f"IMG_{time.strftime('%Y%m%d_%H%M%S')}.png"
        self.ids.camera.export_to_png(f"{path}{filename}")
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = f"{path}{filename}"
        self.manager.current_screen.ids.img.reload()


class ImageScreen(Screen):
    
    """Creates a sharable link for the captured image"""
    def create_link(self):
        """Creates a sharable link for the captured image."""
        file_path = self.ids.img.source
        sharer = FileSharer(filepath=file_path, api_key="A8nIgbg1FSjaq233s5xhkz")
        link = sharer.share()
        self.ids.link.text = f"Link: {link}"
        
        
    def copy_link(self):
        """Copies the generated link to the clipboard."""
        link_text = self.ids.link.text
        if link_text.startswith("Link: "):
            url = link_text[6:]  # Extract only the URL part
            try:
                # Try using pyperclip first (more reliable)
                pyperclip.copy(url)
                print(f"Link copied to clipboard: {url}")
            except Exception as e:
                # Fallback to Kivy's clipboard
                try:
                    Clipboard.copy(url)
                    print(f"Link copied to clipboard (Kivy): {url}")
                except Exception as e2:
                    print(f"Failed to copy to clipboard: {e}, {e2}")
        else:
            print("No valid link to copy")
            
    def open_link(self):
        """Opens the generated link in the default web browser."""
        import webbrowser
        link_text = self.ids.link.text
        if link_text.startswith("Link: "):
            webbrowser.open(link_text[6:])  # Open only the URL part



class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
    
    
MainApp().run()

