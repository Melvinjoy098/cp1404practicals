from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ['Alice', 'Bob', 'Charlie', 'Diana']
        self.create_labels()
        return self.root


    def create_labels(self):
        for name in self.names:
            label = Label(text=name, font_size=32)
            self.root.ids.main.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()