from kivy.app import App
from kivy.lang import Builder


class ConvertMiles(App):
    def build(self):
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMiles().run()