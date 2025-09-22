import requests
import selectorlib

class Temperature:
    
    """Represent a temperature value extracted from the timeanddate.com/weather/ page. """
    
    def __init__(self, country, city):
        self.country = country
        self.city = city
        
    def get(self):
        """Get the temperature from the website"""
        url = f"https://www.timeanddate.com/weather/{self.country}/{self.city}"
        """extract the temperature from the content"""
        request = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        content = request.text
        """this is the selector to extract the temperature"""
        extractor = selectorlib.Extractor.from_yaml_file("temperature.yaml")
        value = extractor.extract(content)["temp"]
        
        if value is None:
            print(f"Could not find temperature for {self.city}")
            return None
            
        print(f"The temperature in {self.city.title()} is {value}")
        # Handle the non-breaking space character (\xa0) before the degree symbol
        self.temperature = float(value.replace('\xa0', ' ').split("°")[0])
        return self.temperature
    
# Example usage:
if __name__ == "__main__":
    temp = Temperature("romania", "bucharest")
    response = temp.get()
    if response:
        print(f"Temperature: {response}°C")