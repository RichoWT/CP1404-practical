from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


FACTOR_MILES_TO_KM = 1.60934


class ConvertMiles(App):

    output_km = StringProperty()

    def build(self):
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, text):
        print("handle calculation")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    def convert_to_number(self, text):
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMiles().run()
