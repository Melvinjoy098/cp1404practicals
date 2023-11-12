from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertMilesKmApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * 1.60934
            self.output_km = str(km)
        except ValueError:
            self.output_km = '0'

    def handle_increment(self, increment):
        try:
            miles = float(self.root.ids.input_miles.text) + increment
            self.root.ids.input_miles.text = str(miles)
        except ValueError:
            self.root.ids.input_miles.text = str(increment)

ConvertMilesKmApp().run()